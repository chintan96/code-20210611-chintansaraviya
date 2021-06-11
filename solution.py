import json
import numpy

f = open('input_data.json') # input json file given
l = json.load(f) # loading json to list
n = numpy.array(l) # converting list to numpy array for better performance


# function to calculate BMI Category and Health Risk from BMI value
def category_risk(bmi):
	if bmi <= 18.4:
		return ['Underweight','Malnutrition']
	elif bmi >= 18.5 and bmi <= 24.9:
		return ['Normal weight','Low Risk']
	elif bmi >= 25 and bmi <= 29.9:
		return ['Overweight','Enhanced Risk']
	elif bmi >= 30 and bmi <= 34.9:
		return ['Moderately obese','Medium Risk']
	elif bmi >= 35 and bmi <= 39.9:
		return ['Severly obese','High Risk']
	elif bmi >= 40:
		return ['Very severle obese','Very High Risk']
	
for i in range(0,len(n)):
	n[i]['BMI'] = round(n[i]['WeightKg']/((n[i]['HeightCm']/100)**2),2) # Calculating BMI from given Formula to 2 decimal values
	temp = category_risk(n[i]['BMI']) # getting BMI Category and Heakth Risk from category_risk function
	n[i]['BMI Category'] = temp[0] # Assingning BMI Category data
	n[i]['Health Risk'] =  temp[1] # Assigning Health Risk Data
	
t = n.tolist() # converting numpy array to list
json_output = json.dumps(t) # converting list to json string
with open('output_data.json','w') as r: # creating a new json output file
	json.dump(json_output,r) # dumping final json data into the output json file
