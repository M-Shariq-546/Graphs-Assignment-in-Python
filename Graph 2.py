from matplotlib import pyplot as plt

x = [1, 2, 3, 4 , 5 , 6 , 7, 8, 9, 10]


y = []

for i in range(1 , 11):
    z = (3 * i)
    y.insert(i , z)

print("Y is = ",y)
print("X is = ",x)

plt.title("Graph of 3X")

plt.plot([1 , 2 ,3, 4, 5, 6 , 7, 8, 9, 10] , [3, 6, 9, 12, 15, 18, 21, 24, 27 , 30])
plt.show()