from urllib.request import urlopen
import json


def json_url():

 response = urlopen("http://188.166.104.86/actions/dcops/device/exercise")

 # storing the JSON response from url in data
 data_json = json.loads(response.read())

 # print the json response
 data = str(data_json['elements']['7d520da4-3283-45bf-98c2-02b371e63a4a']['control']['ports']['top']['voltage'])
 return data

print(json_url())