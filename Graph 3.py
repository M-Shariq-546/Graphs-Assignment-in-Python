from matplotlib import pyplot as plt

x = []
y = []

for i in range(1 , 100):
    x.insert(i , i)

for i in range(1 , 100):
    z = pow(i , 3)
    y.insert(i , z)
    
print("Y is = ",y)
print("X is = ",x)

plt.title("Graph of X^3")
plt.plot(x , y)
plt.show()
