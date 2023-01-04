import matplotlib.pyplot as plt
data={'walking':29,'cycling':15,'car':35,'bus':18,'train':3}
x=list(data.keys())
y=list(data.values())
#fig=plt.figure(figsize=(10,5))
plt.bar(x,y,color="green",width=0.5)

plt.xlabel("mode of transport")
plt.ylabel("frequenxcy")
plt.title("BAR GRAPH")
plt.show()