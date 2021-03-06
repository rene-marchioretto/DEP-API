from urllib.request import urlopen
import json
import re
import datetime 

def json_url():

 today = str(datetime.datetime.now())

 response = urlopen("http://188.166.104.86/actions/dcops/device/exercise")
 data_json = json.loads(response.read())

 data = str(data_json['elements']['7d520da4-3283-45bf-98c2-02b371e63a4a']['control']['ports']['top']['voltage'])
 id = str(data_json['elements'])
 min = str(data_json['elements']['7d520da4-3283-45bf-98c2-02b371e63a4a']['specifications']['ports']['top']['voltage']['min'])
 nom = str(data_json['elements']['7d520da4-3283-45bf-98c2-02b371e63a4a']['specifications']['ports']['top']['voltage']['nom'])
 max = str(data_json['elements']['7d520da4-3283-45bf-98c2-02b371e63a4a']['specifications']['ports']['top']['voltage']['max'])
 if min > data:
     status = 'undervoltage'
 if min < data < nom:
     status = 'below normal'
 if nom < data < max:
     status = 'higher than normal'
 if data > max:
     status = 'higher than max'
 id = str(data_json['elements'])
 id = id.split(":", 1)
 id = re.sub(r'\W+', '', id[0])
 data_set = {'id':id,'voltage': data, 'time':today, 'status': status}
 json_dump = json.dumps(data_set)
 
 return json_dump
