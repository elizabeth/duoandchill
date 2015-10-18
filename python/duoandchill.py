import urllib2
import json
import re
import time
import sys

from firebase import firebase

class user():
    global riot_api
    riot_api = '802644f0-1229-4fe5-94ab-88373a1b7a52'

    #Returns summoner ID of passed ign if it exists. Otherwise raises error.
    def exists(self, ign):
        try:    
            name = ign
            name = name.replace(' ', '%20')
            url = 'https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/' + name + '?api_key=' + riot_api 
            json_obj = urllib2.urlopen(url)
            data = json.load(json_obj)
            return str(data[name.lower().replace('%20', '')]['id'])
        except urllib2.HTTPError, err:
            if err.code == 404:
                return -1
            else:
                raise Exception('error: ' + str(err))

        #Returns link to the passed ign's summoner icon.
    def profileIcon(self, summonerid):
        url = 'https://na.api.pvp.net/api/lol/na/v1.4/summoner/' + summonerid + '?api_key=' + riot_api
        json_obj = urllib2.urlopen(url)
        data = json.load(json_obj)
        iconNum = data[summonerid]['profileIconId']
        return 'http://ddragon.leagueoflegends.com/cdn/5.20.1/img/profileicon/' + str(iconNum) + '.png'

def main_loop():
    users = {}
    while 1:
        Firebase = firebase.FirebaseApplication('https://duoandchill-db.firebaseio.com', None)
        result = Firebase.get('/verified', None,)
        for keys in result:
            if keys not in users:
                p = user()
                users[keys] = p.exists(keys)
            if users[keys] != -1:
                Firebase.patch('/verified/' + keys, {'verified' : 'verified'})
                Firebase.patch('/verified/' + keys, {'summonerId' : users[keys]})
                Firebase.patch('/verified/' + keys, {'summonerIcon' : p.profileIcon(users[keys])})
            else:
                Firebase.patch('/verified/' + keys, {'verified' : 'failed'})
                del users[keys]
        time.sleep(5)

if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print >> sys.stderr, '\nExiting by user request.\n'
        sys.exit(0)


    