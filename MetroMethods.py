import requests
import json


def get_station_info_json(stationcode):
    payload = {'Host':'api.wmata.com','api_key':'6c6320d903d14237b631c93623e1fd71'}
    r = requests.get('https://api.wmata.com/StationPrediction.svc/json/GetPrediction/'+stationcode,payload)
    print r.json()
    return r.json()

def get_path_json(code_from_station,code_to_station):
    payload={'FromStationCode':code_from_station,'ToStationCode':code_to_station,'api_key':'6c6320d903d14237b631c93623e1fd71','Host':'api.wmata.com'}
    url='https://api.wmata.com/Rail.svc/json/jPath'
    r = requests.get(url,payload)
    return r.json()

def get_fare_and_time_json(code_from_station,code_to_station):
    payload={'FromStationCode':code_from_station,'ToStationCode':code_to_station,'api_key':'6c6320d903d14237b631c93623e1fd71','Host':'api.wmata.com'}
    url='https://api.wmata.com/Rail.svc/json/jPath'
    r = requests.get(url,payload)
    return r.json()

#returnes the associated value from json or False
def get_from_json(json_file, key):
    data=json.loads(json_file)
    return data[key]

str = get_path_json("K01","C05");
print str
print get_from_json(str,"StationCode")
