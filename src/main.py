from pandas.tseries import offsets
import requests
import pandas as pd
from marvel_services import MarvelServiceImpl 

marvel_api = MarvelServiceImpl()

id_list = []
description_list = []
modified_list = []
type_list =[]
title_list = []
characters_list = []
characters =[]

#Recuperando Id dos heróis
iron_man = marvel_api.find_character('Iron Man')
thanos = marvel_api.find_character('Thanos')

#Recuperando as Histórias em que contém o personagem Iron Man
stories = marvel_api.find_stories(iron_man.id)

for story in stories:
    id_list.append(story.id)
    title_list.append(story.title)
    description_list.append(story.description)
    type_list.append(story.type)
    modified_list.append(story.modified)
                  
    characters_list.append(story.characters)

#Recuperando as Histórias em que contém o personagem Thanos
stories = marvel_api.find_stories(thanos.id)

for story in stories:
    id_list.append(story.id)
    title_list.append(story.title)
    description_list.append(story.description)
    type_list.append(story.type)
    modified_list.append(story.modified)
                  
    characters_list.append(story.characters)

data = {'id': id_list, 'title':title_list, 'description':description_list, 'type':type_list, 'modified':modified_list, 'characters':characters_list}
df = pd.DataFrame(data=data)
print(df.shape)
df.to_csv('marvel_stories.csv', index=False)