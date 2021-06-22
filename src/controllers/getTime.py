import time
from flask import Flask
from flask_restplus import Api, Resource
from src.server.instance import server
from flask_cors import CORS

app, api = server.app, server.api

data_time = time.gmtime()
curr_time = time.localtime()
CORS(app)

@api.route('/get_time_br')
class Time(Resource):
    def get(self,):
        mon = curr_time.tm_mon
        min = curr_time.tm_min
        if(len(str(mon)) == 1):
            mon = '0'+str(mon)
        if(len(str(min)) == 1):
            min = '0'+str(min)
        data_time = [
            {
                'day': curr_time.tm_mday,
                'mon': mon,
                'year': curr_time.tm_year,
                'hour': curr_time.tm_hour,
                'min': min,
                'sec': curr_time.tm_sec,
             }
        ]
        return data_time



