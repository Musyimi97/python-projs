from collections import OrderedDict

d =OrderedDict()
d['first'] = 1
d['second']=2
d['third'] =3
d['last'] =4

for key in d:
    print(key, d[key])


car ={}
car['wheels']=4
car['model'] ='Porsche'
car['brand'] = 'Cayenne'
car['color'] ='red'

for key in car:
    print (key + ": " +car[key])