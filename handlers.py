import json
import uuid
import random
import requests


from threading import Timer
import time


def btn_exit(hashMap,_files=None,_data=None):
    
    hashMap.put("ShowDialog","Запустить форматирование диска C:?")
    hashMap.put("ShowDialogStyle",json.dumps({"yes":"Выполнить","no":"Отменить","title":"Уточнение"}))
    
    return hashMap            

