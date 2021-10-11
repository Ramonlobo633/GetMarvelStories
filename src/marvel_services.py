import hashlib
from pandas.core.frame import DataFrame
import requests
import json
import logging
import re
import pandas as pd
from math import ceil

from http import HTTPStatus

class Character:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    def __str__(self):
        return self.id + " " + self.name + " " + self.description

class Story:
    def __init__(self, id, title, type, description, modified, characters):
        self.id = id
        self.title = title
        self.type = type
        self.description = description
        self.modified = modified
        self.characters = characters


class MarvelServiceImpl:

    properties = json.load(open('src/config.json'))['propeties']

    # Realiza uma chamada ao Web Service da Marvel API para buscar personagem
    # Retorna um objeto Character
    def find_character(self, name):

        endpoint = self.properties['find_character'].format(name,
                                                       self.properties['public_key'],
                                                       self._generate_hash(),
                                                       self.properties['ts'])
        
        logging.debug('Url a ser chamada no método find_character: {}'.format(endpoint))
        response = requests.get(endpoint)

        if (response.status_code == HTTPStatus.OK):
            response_json = json.loads(response.text)
            if (response_json['code'] == 200):
                data_json = response_json['data']
                total_registros = data_json['total']
                if (total_registros >= 1):
                    resultados_json = data_json['results']
                    marvel_character = resultados_json[0]
                    return Character(marvel_character['id'], marvel_character['name'], marvel_character['description'])
                else:
                    logging.debug('Não foi localizado o personagem')
        else:
            logging.error('Ocorreu um erro ao invocar o WS')


    # Realiza uma chamada ao Web Service da Marvel API para buscar as histórias associadas a um personagem
    # Retorna uma lista de objetos Story
    def find_stories(self, character_id):
        offset = 0
        stories = []
        characters = []
        
        num_iteration = self._get_number_interations(character_id)

        for _ in range(num_iteration):
            endpoint = self.properties['find_stories'].format(character_id,
                                                            self.properties['limit'],
                                                            self.properties['public_key'],
                                                            self._generate_hash(),
                                                            self.properties['ts'],
                                                            offset)
            

            logging.debug('Url a ser chamada no método find_stories: {}'.format(endpoint))
            response = requests.get(endpoint)
                
                
            if (response.status_code == HTTPStatus.OK):
                    
                response_json = json.loads(response.text)
                if (response_json['code'] == 200):
                    data_json = response_json['data']
                    total_registros = data_json['total']
                    
                    if (total_registros >= 1):
                        resultados_json = data_json['results']   
                        
                        for story in resultados_json:
                            [characters.append(character['name']) for character in  story['characters']['items'] ]
                            stories.append(Story(story['id'], story['title'], story['type'], story['description'], story['modified'], characters))
                    else:
                        logging.debug('O serviço não contém histórias associadas ao personagem')
                
            else:
                logging.error('Ocorreu um erro ao invocar o WS')
            offset = offset + int(self.properties['limit'])

        return stories

    # Gera a hash necessária para chamar o Web Service da Marvel API
    def _generate_hash(self):

        return hashlib.md5((self.properties['ts'] + self.properties['private_key'] + self.properties['public_key'])
                           .encode('utf-8')).hexdigest()

    #retorna valor ótimo para quantidade de iterações necessária para recuperar todas stories
    def _get_number_interations(self, character_id):
        endpoint = self.properties['find_stories'].format(character_id,
                                                            self.properties['limit'],
                                                            self.properties['public_key'],
                                                            self._generate_hash(),
                                                            self.properties['ts'],
                                                            '0')
        response = requests.get(endpoint)
            
        if (response.status_code == HTTPStatus.OK):
                
            response_json = json.loads(response.text)
            if (response_json['code'] == 200):
                total = json.loads(response.text)['data']['total']
                if (total >= 1):
                    
                    return ceil(total/int(self.properties['limit']))
                    
                else:
                    logging.debug('O serviço não contém histórias associadas ao personagem')
                    return 0

        else:
            logging.error('Ocorreu um erro ao invocar o WS')
