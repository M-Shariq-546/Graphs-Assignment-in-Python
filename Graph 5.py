from matplotlib import pyplot as plt

x = [1, 2, 3, 4 , 5 , 6 , 7, 8, 9, 10]


y = []

for i in range(1 , 11):
    z = (2 * pow(i , 2)) + (3 * i)
    y.insert(i , z)
    
print("Y is = ",y)
print("X is = ",x)
plt.title("Graph of 2X^2+3X")
plt.plot([1, 2, 3, 4 , 5 , 6 , 7, 8, 9, 10] , [5, 14, 27, 44, 65, 90, 119, 152, 189, 230])
plt.show()