# FakerJSONDataGenerator

from faker import Faker
import json		
from random import randint	
fake = Faker()

def alarm(x)

def input_data(x):
	# dictionary
	sensor_data ={}
	for i in range(1, x):
		sensor_data[i]={}
		sensor_data[i]['ObjectID_1']= i
		sensor_data[i]['Fullness_Percent']= randint(1, 100)
		sensor_data[i]['Gas_Sensor_Activity']= fake.boolean(chance_of_getting_true=50)
		sensor_data[i]['Temperature']= randint(1, 100)
	print(sensor_data)

	# dictionary dumped as json in a json file
	with open('cop_toplama.json', 'w') as fp:
		json.dump(sensor_data, fp)

def main():

	# Enter number of students
	# For the above task make this 100
	number_of_sensors = 32
	input_data(number_of_sensors)
main()
# The folder or location where this python code
# is save there a json data


Results 

{
   "1":{
      "ObjectID_1":1,
      "Fullness_Percent":41,
      "Gas_Sensor_Activity":false,
      "Temperature":3
   },
   "2":{
      "ObjectID_1":2,
      "Fullness_Percent":15,
      "Gas_Sensor_Activity":false,
      "Temperature":94
   },
   "3":{
      "ObjectID_1":3,
      "Fullness_Percent":46,
      "Gas_Sensor_Activity":true,
      "Temperature":42
   },
   "4":{
      "ObjectID_1":4,
      "Fullness_Percent":60,
      "Gas_Sensor_Activity":true,
      "Temperature":71
   },
   "5":{
      "ObjectID_1":5,
      "Fullness_Percent":47,
      "Gas_Sensor_Activity":true,
      "Temperature":30
   },
   "6":{
      "ObjectID_1":6,
      "Fullness_Percent":47,
      "Gas_Sensor_Activity":true,
      "Temperature":94
   },
   "7":{
      "ObjectID_1":7,
      "Fullness_Percent":71,
      "Gas_Sensor_Activity":true,
      "Temperature":82
   },
   "8":{
      "ObjectID_1":8,
      "Fullness_Percent":27,
      "Gas_Sensor_Activity":true,
      "Temperature":29
   },
   "9":{
      "ObjectID_1":9,
      "Fullness_Percent":34,
      "Gas_Sensor_Activity":false,
      "Temperature":6
   },
   "10":{
      "ObjectID_1":10,
      "Fullness_Percent":58,
      "Gas_Sensor_Activity":true,
      "Temperature":52
   },
   "11":{
      "ObjectID_1":11,
      "Fullness_Percent":89,
      "Gas_Sensor_Activity":false,
      "Temperature":18
   },
   "12":{
      "ObjectID_1":12,
      "Fullness_Percent":95,
      "Gas_Sensor_Activity":false,
      "Temperature":59
   },
   "13":{
      "ObjectID_1":13,
      "Fullness_Percent":62,
      "Gas_Sensor_Activity":false,
      "Temperature":89
   },
   "14":{
      "ObjectID_1":14,
      "Fullness_Percent":83,
      "Gas_Sensor_Activity":false,
      "Temperature":92
   },
   "15":{
      "ObjectID_1":15,
      "Fullness_Percent":46,
      "Gas_Sensor_Activity":true,
      "Temperature":34
   },
   "16":{
      "ObjectID_1":16,
      "Fullness_Percent":21,
      "Gas_Sensor_Activity":true,
      "Temperature":90
   },
   "17":{
      "ObjectID_1":17,
      "Fullness_Percent":91,
      "Gas_Sensor_Activity":false,
      "Temperature":35
   },
   "18":{
      "ObjectID_1":18,
      "Fullness_Percent":92,
      "Gas_Sensor_Activity":false,
      "Temperature":72
   },
   "19":{
      "ObjectID_1":19,
      "Fullness_Percent":48,
      "Gas_Sensor_Activity":true,
      "Temperature":39
   },
   "20":{
      "ObjectID_1":20,
      "Fullness_Percent":58,
      "Gas_Sensor_Activity":false,
      "Temperature":53
   },
   "21":{
      "ObjectID_1":21,
      "Fullness_Percent":100,
      "Gas_Sensor_Activity":false,
      "Temperature":52
   },
   "22":{
      "ObjectID_1":22,
      "Fullness_Percent":97,
      "Gas_Sensor_Activity":false,
      "Temperature":48
   },
   "23":{
      "ObjectID_1":23,
      "Fullness_Percent":63,
      "Gas_Sensor_Activity":false,
      "Temperature":71
   },
   "24":{
      "ObjectID_1":24,
      "Fullness_Percent":31,
      "Gas_Sensor_Activity":false,
      "Temperature":100
   },
   "25":{
      "ObjectID_1":25,
      "Fullness_Percent":53,
      "Gas_Sensor_Activity":true,
      "Temperature":77
   },
   "26":{
      "ObjectID_1":26,
      "Fullness_Percent":37,
      "Gas_Sensor_Activity":true,
      "Temperature":19
   },
   "27":{
      "ObjectID_1":27,
      "Fullness_Percent":67,
      "Gas_Sensor_Activity":false,
      "Temperature":91
   },
   "28":{
      "ObjectID_1":28,
      "Fullness_Percent":49,
      "Gas_Sensor_Activity":false,
      "Temperature":76
   },
   "29":{
      "ObjectID_1":29,
      "Fullness_Percent":49,
      "Gas_Sensor_Activity":false,
      "Temperature":58
   },
   "30":{
      "ObjectID_1":30,
      "Fullness_Percent":75,
      "Gas_Sensor_Activity":false,
      "Temperature":62
   },
   "31":{
      "ObjectID_1":31,
      "Fullness_Percent":54,
      "Gas_Sensor_Activity":false,
      "Temperature":63
   }
}
