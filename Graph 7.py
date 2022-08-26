from matplotlib import pyplot as plt

x = []
y = []
y1 = []

for i in range(1 , 1500):
    x.insert(i , i)

for i in range(1 , 1500):
    z = pow(i , 2)
    y.insert(i , z)

for i in range(1 , 1500):
    z = 1000 * i
    y1.insert(i , z)

print("X is = ",x)
print("Y is = ",y)
print("Y1 is = ",y1)

plt.title("Graph of X^2 and 1000X")
plt.plot(x , y)
plt.plot(x , y1)
plt.show()
