from matplotlib import pyplot as plt
import numpy 
x = [1, 2, 3, 4 , 5 , 6 , 7, 8, 9, 10]


y = []

for i in range(1 , 11):
    z =numpy.log(i)
    y.insert(i , z)
    
print("Y is = ",y)
print("X is = ",x)

plt.title("Graph of LogX")
plt.plot([1, 2, 3, 4 , 5 , 6 , 7, 8, 9, 10] , [0.0, 0.6931471805599453, 1.0986122886681098, 1.3862943611198906, 1.6094379124341003, 1.791759469228055, 1.9459101490553132, 2.0794415416798357, 2.1972245773362196, 2.302585092994046])
plt.show()
