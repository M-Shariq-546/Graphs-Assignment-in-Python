from matplotlib import pyplot as plt

x = [1, 2, 3, 4 , 5 , 6 , 7, 8, 9, 10]


y = []

for i in range(1 , 11):
    z = pow(i , 3)
    y.insert(i , z)
    
print("Y is = ",y)
print("X is = ",x)

plt.title("Graph of X^3")
plt.plot([1, 2, 3, 4 , 5 , 6 , 7, 8, 9, 10] , [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000])
plt.show()