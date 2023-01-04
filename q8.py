import matplotlib.pyplot as plt
xpoints=['mon','tue','wed','thu','fri']
ypoints=[300,4050,150,400,650]
plt.subplot(1,2,1)
plt.grid(color='blue',linestyle="dotted")

plt.xlabel("days of week")
plt.ylabel("sale of drinks")
plt.title("sales data1",loc='right')

plt.plot(xpoints,ypoints,linestyle="dotted",color='cyan',marker="h",mfc="m",mec="black")


ypoints=[400,500,350,300,500]
plt.subplot(1,2,2)
plt.grid(color="blue",linestyle="dotted")
plt.xlabel("days of week")
plt.ylabel("sale of food")
plt.title("sales data2",loc='center')
plt.plot(xpoints,ypoints,linestyle="dashed",color="yellow",marker="d",mfc="g",mec="r")
plt.show()