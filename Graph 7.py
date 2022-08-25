from matplotlib import pyplot as plt

x = [1, 2, 3, 4 , 5 , 6 , 7, 8, 9, 10]


y = []
y1= []
for i in range(1 , 11):
    z = pow(i , 2)
    y.insert(i , z)
    
for i in range(1 ,11):
    z = 1000 * i
    y1.insert(i , z)


print("Y is = ",y)
print("X is = ",x)
print("Y1 is = ",y1)

plt.title("Graph of X^2 and 1000*X")
plt.plot([1, 2, 3, 4 , 5 , 6 , 7, 8, 9, 10] , [1, 4, 9, 16, 25, 36, 49, 64, 81, 100])
plt.plot([1, 2, 3, 4 , 5 , 6 , 7, 8, 9, 10] , [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000])
plt.show()