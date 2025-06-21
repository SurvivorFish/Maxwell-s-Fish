import matplotlib.pyplot as plt

MegaFile = open('Graph data/Data.txt', 'r')

GraphTime = []
Et = []
St = []
Tt = []
Tdt = []
Nl = []
Nr = []

for s in MegaFile:
    strings = s.split(' ')
    GraphTime.append(float(strings[0]))
    Et.append(float(strings[1]))
    St.append(float(strings[2]))
    Tt.append(float(strings[3]))
    Tdt.append(float(strings[4]))
    Nl.append(float(strings[5]))
    Nr.append(float(strings[6]))

plt.figure()
plt.plot(GraphTime, Et)
plt.show()
plt.plot(GraphTime, St)
plt.show()
plt.plot(GraphTime, Tt)
plt.show()
plt.plot(GraphTime, Tdt)
plt.show()
plt.plot(GraphTime, Nl)
plt.show()
plt.plot(GraphTime, Nr)
plt.show()