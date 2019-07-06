from app import log, spc
from bs4 import BeautifulSoup
import requests, json

def mergestr(*args):
    return "".join([c for c in ''.join(args) if c.isalpha() == True]).lower() 


def get():
    return [dashboard for dashboard in 
            json.loads(requests.get('https://' + spc['host'] + 
                        ':8089/servicesNS/' + spc['user'] + 
                        '/splunkb_templates/data/ui/views/', 
                        data={'output_mode': 'json'}, 
                        auth=(spc['user'], spc['password']), 
                        verify=False).text)['entry'] 
                        
            if dashboard['acl']['app'] == 'splunkb_templates']


def parse(dashboard):

    soup = BeautifulSoup(dashboard['content']['eai:data'], 'xml')
    mainsearch = [search for search in soup.find_all('search') if 'base' not in search.attrs.keys()]
    subsearches = [search for search in soup.find_all('search') if 'id' in search.attrs.keys() and 'base' in search.attrs.keys()]
    basesearches = [search for search in soup.find_all('search') if ('id' not in search.attrs.keys() and 'base' in search.attrs.keys())]
    panels = []
    
    def gg(i, search, bs):
        panels.append({'query': str(mainsearch[0].query.text + 
                                (i.query.text if bs is True else '') + 
                                (search.query.text if search.query else '')
                                ).replace('\n', '').replace('     ',''), 
                        'dashboard': mergestr(dashboard['name']),
                        'title': search.parent.parent.title.text,
                        'namespace': mergestr(dashboard['name'], search.parent.parent.title.text, search.parent.name),
                        'ptype': search.parent.name})

    for search in basesearches:
        if len(subsearches) > 0:
            [gg(i, search, True) for i in list(filter(lambda s: s.attrs['id'] == search.attrs['base'], subsearches))]
        else:
            [gg(i, search, False) for i in list(filter(lambda s: s.attrs['id'] == search.attrs['base'], mainsearch))]

    return panels

def compare():
    for dashboard in get():
        log.warn( parse(dashboard) )
        
