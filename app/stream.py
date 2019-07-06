from app import socketio, dashboards, log
from app.integration import Splunk, DB
from multiprocessing import Process
import time, json


def mngtopan(dashboard, panel):
    log.warn('[' + dashboard['name'] + ']' + panel['title'] + ' Mongo Transmitting...')
    namespace = dashboards.mergestr(dashboard['name'], panel['title'], panel['ptype'])
    db = DB(namespace)

    # while True:
    #     try:
    #         socketio.emit('events', {'data': db.collection.find({}, {"_id": 0}).limit(1).sort({'$natural':-1})}, 
    #                       namespace='/' + namespace)

    #     except Exception as e:
    #         log.warn('[' + dashboard['name'] + '][' + panel['title'] + ']' + str(e))
        
    #     time.sleep(5)


# Отправка данных из Splunk панели в Mongodb в соответствующую коллекцию. Так же отправка статуса об 
# успешном запросе в Splunk. Подключение к Mongodb и Splunk происходит один раз во время открытия процесса. 
# Важно удалить job в Splunk в конце итерации. Коллекция в Mongodb и Namespace в Socketio генерируется уникально 
# для панели на базе её параметров. Стриминг происходит с общим таймаутом в 5 сек. 
# После создания job в Splunk необходимо ждать не менее 2 сек (при любой сложности).
def ptmongo(dashboard, panel):
    log.warn('[' + dashboard['name'] + ']' + panel['title'] + ' Splunk Transmitting...')

    namespace = dashboards.mergestr(dashboard['name'], panel['title'], panel['ptype'])

    splunk = Splunk()
    db = DB(namespace)
    while True:
        try:
            job = splunk.service.jobs.create(panel['query'])
            time.sleep(3)
            results =  [u for u in splunk.results.ResultsReader(splunk.service.jobs[job.sid].preview(**{"count":100}))]

            for r in results:
                db.col.update(r, r, upsert=True)

            socketio.emit('status', {'on': True}, namespace='/' + namespace)
            job.cancel()

        except Exception as e:
            log.warn('[' + dashboard['name'] + '][' + panel['title'] + ']' + str(e))
            socketio.emit('status', {'on': False}, namespace='/' + namespace)
        
        time.sleep(2)


def watch_dashboard(dashboard):
    log.warn('[' + dashboard['name'] + '] Watching...')

    [Process(target=ptmongo, 
            args=(dashboard, panel)).start() 
            for panel in dashboards.parse(dashboard) 
            if panel['query'] !='empty']

    [Process(target=mngtopan, 
            args=(dashboard, panel)).start() 
            for panel in dashboards.parse(dashboard) 
            if panel['query'] !='empty']


def watchdog():
        log.warn('[LAUNCH] Monitoring dashboards')

        [Process(target=watch_dashboard, 
                 name=dashboard['name'], 
                 args=(dashboard,)).start() 
                 for dashboard in dashboards.get()]
                

Process(target=watchdog, name="jobs_watchdog").start()
