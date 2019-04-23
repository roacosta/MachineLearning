import matplotlib.pyplot as plt
from sklearn import datasets as ds

iris = ds.load_iris()
iris_data = iris.data
iris_target = iris.target

color = (['r','g','b'])

for i in range(iris_data.shape[1]):
	for j in range(i + 1,iris_data.shape[1]):
		for k in range(len(iris.target_names)):		
			plt.scatter(iris_data[iris_target==k,i],iris_data[iris_target==k,j],color=color[k],label=iris.target_names[k])

		plt.xlabel(iris.feature_names[i])
		plt.ylabel(iris.feature_names[j])
		plt.legend()
		plt.show()
	
