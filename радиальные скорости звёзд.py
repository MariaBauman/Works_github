import matplotlib.pyplot as plt

file = 'star'
data = open(file, "r")
lines = data.readlines()
del lines[0] # удалила заголовки
data.close()

x = [] # дата
y = [] # скорости

for i in lines:
    x.append(float(i.split(' ')[0]))

for j in lines:
    j = j.strip()
    y.append(float(j.split(' ')[1]))

#y.sort(key=lambda y1: (y1))
#x.sort(key=lambda x1: (x1))
plt.figure()
plt.scatter(x, y)
plt.xlabel('MJD')
plt.ylabel('Vr')
plt.title('Зависимость радиальной скорости звезды от юлианской даты')
plt.show()






