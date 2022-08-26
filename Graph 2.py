from matplotlib import pyplot as plt

x = []
y = []

for i in range(1 , 100):
    x.insert(i , i)

for i in range(1 , 100):
    z = 3 * i
    y.insert(i , z)
    
print("Y is = ",y)
print("X is = ",x)

plt.title("Graph of 3X")
plt.plot(x , y)
plt.show()
