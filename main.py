from faker import Faker
import json		
from random import randint	
fake = Faker()

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
