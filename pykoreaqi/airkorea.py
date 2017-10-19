import requests
import json
from time import sleep

METRIC_TO_CODE ={'PM10':'10007',
                 'PM25':'10008',
                 'O3':'10003',
                 'NO2':'10006',
                 'CO':'10002',
                 'SO2':'10001',
                 'CAI':'KHAI'}

class AirKorea():
    def __init__(self):
        self.base_url ='http://www.airkorea.or.kr'
        #TODO pass in custom headers and/or proxy settings here
        
    def _get_metric_realtime(self,metric_id):
        '''get raw json from xhr request at site'''
        
        #TODO add proper headers
        if metric_id not in METRIC_TO_CODE:
            raise KeyError('invalid metric: possible values are: %s'%', '.join(METRIC_TO_CODE.keys()))
            
        url = self.base_url + '/eng/real/tab1Search?itemCode=%s'%METRIC_TO_CODE[metric_id]
        
        r = requests.get(url)
        r.raise_for_status()
        
        data = json.loads(r.content)
        return data.get('tab1',[])
        
    def get_all_realtime(self, delay=.1,metrics=None):
        ''''''
        station_keys = ['ENG_STATION_ADDR','STATION_ADDR','STATION_CODE','STATION_NAME','DM_X','DM_Y']
        measurement_keys = ['AVG24','BASE','GRADE','VALUE','DATA_TIME']
        stations={}
        
        if metrics is None:
            metrics = METRIC_TO_CODE.keys()
        
        #TODO: add retry logic
        #TODO: rename some keys like DM_X, DM_Y etc to lat/long 
        all_data=[]
        for metric in metrics:
            data = self._get_metric_realtime(metric)
            sleep(delay)
            all_data.append(data)

        #format the results into a non flat format
        for metric,data in zip(metrics,all_data):
            for row in data:
                #fill in the location information if we don't have it already
                station_code = row['STATION_CODE']
                if station_code not in stations:
                    new_station = dict( (k,row.get(k,None)) for k in station_keys)
                    stations[station_code] = new_station
                    stations[station_code]['MEASUREMENT']=[]

                #add the measurement
                new_measurement = dict( (k,row.get(k,None)) for k in measurement_keys )
                new_measurement['METRIC'] = metric
                stations[station_code]['MEASUREMENT'].append(new_measurement)

        #return a list without the station code (since it is basically an internal identifier)
        return [ stations[k] for k in stations]        