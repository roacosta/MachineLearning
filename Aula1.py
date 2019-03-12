import numpy as np

AQ = np.genfromtxt('AirQualityUCI.csv',delimiter=';',dtype='str',skip_header=1) ## CARREGA OS DADOS

AQ = AQ[:,:-2] ##REMOVE AS DUAS ULTIMAS COLUNAS

AQ = AQ[:,2:] ##REMOVE AS DUAS PRIMEIRAS COLUNAS


## forma não pythonica

##for i in range(AQ.shape[0]):
##	if np.count_nonzero(i):
##		break
		
## forma pythonica

i = np.nonzero(AQ=='')[0][0]

AQ = AQ[:i,:]
		


