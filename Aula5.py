import numpy as np
import matplotlib.pyplot as plt
import sys
from sklearn import linear_model


IrisDefault = np.genfromtxt('iris.data',delimiter=',',dtype='str') ## CARREGA OS DADOS

#for i in range(0,IrisDefault.shape[0]):
#	print(IrisDefault[i][4])
IrisCodificada = IrisDefault
IrisCodificada[IrisCodificada == 'Iris-setosa'] = '0'
IrisCodificada[IrisCodificada == 'Iris-versicolor'] = '1'
IrisCodificada[IrisCodificada == 'Iris-virginica'] = '2'

np.random.seed(2)
np.random.shuffle(IrisCodificada)

IrisData = IrisCodificada[:,:-1].astype(float)

y=IrisCodificada[:,-1]
y=np.reshape(np.array(y,dtype=int),(len(y),1))

nsize=int(IrisData.shape[0]*.4)

IrisTrain = IrisData[:nsize,:]
IrisTest  = IrisData[nsize:,:]
yTrain 		= y[:nsize]		
yTest		= y[nsize:]


r			=	linear_model.LogisticRegression()
yTrain		=	np.ravel(yTrain)
r.fit(IrisTrain,yTrain)
yTest		=	np.ravel(yTest)

print('Iris Learner:')

y_hat		=	r.predict(IrisTrain)
print('   Taxa de acerto (treino) setosa      :', np.mean((y_hat==0)==(yTrain==0)))
print('   Taxa de acerto (treino) versicolor  :', np.mean((y_hat==1)==(yTrain==1)))
print('   Taxa de acerto (treino) virginica   :', np.mean((y_hat==2)==(yTrain==2)))


y_hat=r.predict(IrisTest)
print('\n   Taxa de acerto (teste)  setosa      :', np.mean((y_hat==0)==(yTest==0)))
print('   Taxa de acerto (teste)  versicolor  :', np.mean((y_hat==1)==(yTest==1)))
print('   Taxa de acerto (teste)  virginica   :', np.mean((y_hat==2)==(yTest==2)))










	
	

