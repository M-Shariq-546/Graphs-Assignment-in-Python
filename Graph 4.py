from matplotlib import pyplot as plt

x = [1, 2, 3, 4 , 5 , 6 , 7, 8, 9, 10]


y = []

for i in range(0 , 10):
    z =1 / pow(2 , i)
    y.insert(i , z)
    y.reverse()
    
print("Y is = ",y)
print("X is = ",x)

plt.title("Graph of LogX")
plt.plot([1, 2, 3, 4 , 5 , 6 , 7, 8, 9, 10] , [0.001953125, 0.0078125, 0.03125, 0.125, 0.5, 1.0, 0.25, 0.0625, 0.015625, 0.00390625])
plt.show()