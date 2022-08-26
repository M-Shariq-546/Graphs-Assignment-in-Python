from matplotlib import pyplot as plt
import numpy
x = []
y = []

for i in range(1 , 100):
    x.insert(i , i)

for i in range(1 , 100):
    z = numpy.log(i)
    y.insert(i , z)
    
print("Y is = ",y)
print("X is = ",x)

plt.title("Graph of logX")
plt.plot(x , y)
plt.show()
