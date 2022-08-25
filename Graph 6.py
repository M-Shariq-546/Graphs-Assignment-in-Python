from matplotlib import pyplot as plt

x = [1, 2, 3, 4 , 5 , 6 , 7, 8, 9, 10]


y = []

for i in range(1 , 11):
    z = (3 * i) + 2
    y.insert(i , z)
    
print("Y is = ",y)
print("X is = ",x)
plt.title("Graph of 3*X + 2")
plt.plot([1, 2, 3, 4 , 5 , 6 , 7, 8, 9, 10] , [5, 8, 11, 14, 17, 20, 23, 26, 29, 32])
plt.show()