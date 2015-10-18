# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 20:45:34 2015

@author: rickyschai
"""

import urllib2
import json
import re

riot_api = '81a78d77-5aee-4133-bf67-b34f05295fa3'


#Returns summoner ID of passed ign if it exists. Otherwise raises error.
def exists(ign):
    try:    
        name = ign
        name = name.replace(' ', '%20')
        url = 'https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/' + name + '?api_key=' + riot_api 
        json_obj = urllib2.urlopen(url)
        data = json.load(json_obj)
        return data[name.lower().replace('%20', '')]['id']
    except urllib2.HTTPError, err:
        if err.code == 404:
            raise Exception('summoner does not exist')
        else:
            raise Exception('error: ' + err)

#Returns level of passed ign.
def level(ign): 
    summonerid = exists(ign)
    url = 'https://na.api.pvp.net/api/lol/na/v1.4/summoner/' + str(summonerid) + '?api_key=' + riot_api
    json_obj = urllib2.urlopen(url)
    data = json.load(json_obj)
    return data[str(summonerid)]['summonerLevel']
    

#Returns rank of passed ign. Returns unranked if not ranked. 
def rank(ign):      
    try:
        if level(ign) != 30:
            return 'not level 30'
        summonerid = str(exists(ign))
        url = 'https://na.api.pvp.net/api/lol/na/v2.5/league/by-summoner/' + summonerid + '/entry?api_key=' + riot_api
        json_obj = urllib2.urlopen(url)
        data = json.load(json_obj)
        if (str(data[summonerid][0]['queue']) == 'RANKED_SOLO_5x5'):
            return str(data[summonerid][0]['tier'])
        return 'unranked'
    except urllib2.HTTPError, err:
        if err.code == 404:
            return 'unranked'
        else:
            raise Exception('error: ' + err)

#Returns whether player 1 and player 2 are within one division of each other. Unranked is defaulted as Silver. 
def canDuo(player1, player2):    
    ranks = ['BRONZE', 'SILVER', 'GOLD', 'PLATINUM', 'DIAMOND', 'MASTER', 'CHALLENGER']
    player1rank = rank(player1)
    player2rank = rank(player2)  
    if player1rank == 'unranked':
        player1rank = 'SILVER'
    if player2rank == 'unranked':
        player2rank = 'SILVER'
    if player1rank == 'not level 30' or player2rank == 'not level 30':
        return False
    return abs(ranks.index(player1rank) - ranks.index(player2rank)) < 2

#Returns link to image of a champion.
def championImage(champion):
    return 'http://ddragon.leagueoflegends.com/cdn/5.20.1/img/champion/' + champion + '.png'

#Returns champion names that correspond to the keyword used in the URL for champion images in alphbetical order in championImageList.txt
def championImageList():
    url = 'https://global.api.pvp.net/api/lol/static-data/na/v1.2/versions?api_key=81a78d77-5aee-4133-bf67-b34f05295fa3'
    json_obj = urllib2.urlopen(url)
    data = json.load(json_obj)
    version = data[0]
    url = 'http://ddragon.leagueoflegends.com/cdn/' + version() + '/data/en_US/champion.json'
    json_obj = urllib2.urlopen(url)
    data = json.load(json_obj)
    championDict = data['data']
    orderedList = []
    for keys in championDict:
        orderedList.append(keys)
    orderedList.sort()
    f = open('championImageList.txt', 'w')
    for keys in orderedList:
        print >> f, keys
    f.close()

#Returns in game champion names in alphabetical order in championList.txt
def championList():
    url = 'http://ddragon.leagueoflegends.com/cdn/' + version + '/data/en_US/champion.json'
    json_obj = urllib2.urlopen(url)
    data = json.load(json_obj)
    championDict = data['data']
    orderedList = []
    for keys in championDict:
        orderedList.append(championDict[keys]['name'])
    orderedList.sort()
    f = open('championList.txt', 'w')
    for keys in orderedList:
        print >> f, keys
    f.close()

#Returns link to the passed ign's summoner icon.
def profileIcon(ign):
    summonerid = str(exists(ign))
    url = 'https://na.api.pvp.net/api/lol/na/v1.4/summoner/' + summonerid + '?api_key=' + riot_api
    json_obj = urllib2.urlopen(url)
    data = json.load(json_obj)
    iconNum = data[summonerid]['profileIconId']
    return 'http://ddragon.leagueoflegends.com/cdn/' + version() + '/img/profileicon/' + str(iconNum) + '.png'

#Returns the current version of League.
def version():
    url = 'https://global.api.pvp.net/api/lol/static-data/na/v1.2/versions?api_key=' + riot_api
    json_obj = urllib2.urlopen(url)
    data = json.load(json_obj)
    return data[0]
    




    
