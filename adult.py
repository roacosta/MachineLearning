import numpy as np
import pandas as pd
"""Listing of attributes: 

>50K, <=50K. 

0  age: continuous. 
1  workclass: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked. 
2  fnlwgt: continuous. 
3  education: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool. 
4  education-num: continuous. 
5  marital-status: Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse. 
6  occupation: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces. 
7  relationship: Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried. 
8  race: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black. 
9  sex: Female, Male. 
10 capital-gain: continuous. 
11 capital-loss: continuous. 
12 hours-per-week: continuous. 
13 native-country: United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands."""

#Carrega os dados
Adult = np.genfromtxt('adult.data',delimiter=',',dtype='str')


for i in range(Adult.shape[1]-1):
	coluna = Adult[:,i]
	atributos = pd.value_counts(coluna)
	Adult[Adult[:,i]==' ?',i] = atributos.idxmax()
	
	

workclass = np.unique(Adult[:,1])
for i in range(workclass.shape[0]):
	Adult[Adult[:,1] == workclass[i],1] = i
	
education = np.unique(Adult[:,3])
for i in range(education.shape[0]):
	Adult[Adult[:,3] == education[i],3] = i
	
marital = np.unique(Adult[:,5])
for i in range(marital.shape[0]):
	Adult[Adult[:,5] == marital[i],5] = i

occupation = np.unique(Adult[:,6])
for i in range(occupation.shape[0]):
	Adult[Adult[:,6] == occupation[i],6] = i
	
relationship = np.unique(Adult[:,7])
for i in range(relationship.shape[0]):
	Adult[Adult[:,7] == relationship[i],7] = i
	
race = np.unique(Adult[:,8])
for i in range(race.shape[0]):
	Adult[Adult[:,8] == race[i],8] = i
	
sex = np.unique(Adult[:,9])
for i in range(sex.shape[0]):
	Adult[Adult[:,9] == sex[i],9] = i
	
native = np.unique(Adult[:,13])
for i in range(native.shape[0]):
	Adult[Adult[:,13] == native[i],13] = i
	

	
