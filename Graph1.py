from matplotlib import pyplot as plt

x = [1, 2, 3, 4 , 5 , 6 , 7, 8, 9, 10]

y = []
for i in range(1 , 11):
    z = (2 * i)
    y.insert(i , z)

print("Y is = ",y)
print("X is = ",x)
 
plt.title("Graph of 2X")
plt.plot([1,2,3,4,5,6,7,8,9,10] , [2,4 , 6, 8,10 , 12 , 14 , 16 , 18 , 20])
plt.show()