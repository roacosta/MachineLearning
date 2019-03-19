import numpy as np
import pandas as pd

AQ = np.genfromtxt('AirQualityUCI.csv',delimiter=';',dtype='str',skip_header=1) ## CARREGA OS DADOS

AQ = AQ[:,:-2] ##REMOVE AS DUAS ULTIMAS COLUNAS

AQ = AQ[:,2:] ##REMOVE AS DUAS PRIMEIRAS COLUNAS


## forma não pythonica

##for i in range(AQ.shape[0]):
##	if np.count_nonzero(i):
##		break
		
## forma pythonica

i = np.nonzero(AQ=='')[0][0] #

AQ = AQ[:i,:]

# Versão não pythonica
#y = AQ[:,3]

#AQ = np.delete(AQ,3,axis=1)

#for i in range(y.shape[0]):
#	y[i] = y[i].replace(',','.')
	
#y = y.astype(float)

#Versão pythonica:

y=[float(label.replace(',','.')) for label in AQ[:,3]]

AQTeste = np.char.replace(AQ,',','.').astype(float)

#Xpd = pd.DataFrame(AQTeste)
#Xpd = Xpd.interpolate(AQTeste)
#Xpd = np.array(Xpd)

d=AQTeste.shape[1] ## d must be updated (some features were deleted)
for i in range(d):
	avg = np.mean(AQTeste[np.nonzero(AQTeste[:,i]!=-200),i])
	AQTeste[np.nonzero(AQTeste[:,i]==-200),i]=avg

finaldata = np.insert(AQTeste,d,y,axis=1)
np.savetxt('AirQualityFinal.csv',finaldata,delimiter=';')




