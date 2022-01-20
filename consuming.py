#imported for schedule the time that the request is made from the api
from apscheduler.schedulers.blocking import BlockingScheduler as scheduler
#imported to clean some data
import re
#imported to request the proposed url
from urllib.request import urlopen
#imported to work with json 
import json
#imported to to retrieve the current time
import datetime 

#creating a def for retrieving a organized json from the information sent by the DC/DC converter in a rescursive way and saving in a json file
def json_url():
 #extract the time and date from the request
 today = str(datetime.datetime.now())

 #retrieve the data from the url and store in data_json variable
 response = urlopen("http://188.166.104.86/actions/dcops/device/exercise")
 data_json = json.loads(response.read())

 #formating the json for proper use of information
 data = str(data_json['elements']['7d520da4-3283-45bf-98c2-02b371e63a4a']['control']['ports']['top']['voltage'])
 id = str(data_json['elements'])
 min = str(data_json['elements']['7d520da4-3283-45bf-98c2-02b371e63a4a']['specifications']['ports']['top']['voltage']['min'])
 nom = str(data_json['elements']['7d520da4-3283-45bf-98c2-02b371e63a4a']['specifications']['ports']['top']['voltage']['nom'])
 max = str(data_json['elements']['7d520da4-3283-45bf-98c2-02b371e63a4a']['specifications']['ports']['top']['voltage']['max'])

 #create a status parameter based in the voltage parameters and the data extracted
 if min > data:
     status = 'undervoltage'
 if min < data < nom:
     status = 'below normal'
 if nom < data < max:
     status = 'higher than normal'
 if data > max:
     status = 'higher than max'
 
 #extract id parameters from json and formatting to better display
 id = str(data_json['elements'])
 id = id.split(":", 1)
 id = re.sub(r'\W+', '', id[0])

 #creating the json using the data retrieved from the original json
 data_set = {'id':id,'voltage': data, 'time':today, 'status': status}
 json_dump = json.dumps(data_set)

 #creating a json file with all the data retrieved
 with open("voltage: {}.json".format(today), "w") as f:
    f.write(json_dump)

 return json_dump

#import the scheduler class, define the interval in 5 seconds and initialize the application
sch = scheduler()
sch.add_job(json_url, 'interval', seconds=5)
sch.start()