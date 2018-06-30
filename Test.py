import json
#import sys
#print ('\n'.join(sys.path))
from scipy import spatial

with open('TartanTestOne.json') as fp:
    data = json.load(fp)

with open('TartanTestTwo.json') as fp:
    Two = json.load(fp)

with open('TartanHallWay.json') as fp:
    Bad = json.load(fp)
#Initiating lists
One_T_X = []
One_T_Y = []
One_T_Z = []
Two_T_X = []
Two_T_Y = []
Two_T_Z = []
Three_T_X = []
Three_T_Y = []
Three_T_Z = []


for i in range(712, 821):
    One_T_X = One_T_X + [(data['MagTest']['Admin'][f"{i}"]['fieldTesla']['x'])]
    One_T_Y = One_T_Y + [(data['MagTest']['Admin'][f"{i}"]['fieldTesla']['y'])]
    One_T_Z = One_T_Z + [(data['MagTest']['Admin'][f"{i}"]['fieldTesla']['z'])]
    One_M_X = (data['MagTest']['Admin'][f"{i}"]['magnetometer']['x'])
    One_M_Y = (data['MagTest']['Admin'][f"{i}"]['magnetometer']['y'])
    One_M_Z = (data['MagTest']['Admin'][f"{i}"]['magnetometer']['z'])

for j in range(823, 946):
    Two_T_X = Two_T_X + [(Two['MagTest']['Admin'][f"{j}"]['fieldTesla']['x'])]
    Two_T_Y = Two_T_Y + [(Two['MagTest']['Admin'][f"{j}"]['fieldTesla']['y'])]
    Two_T_Z = Two_T_Z + [(Two['MagTest']['Admin'][f"{j}"]['fieldTesla']['z'])]
    Two_M_X = (Two['MagTest']['Admin'][f"{j}"]['magnetometer']['x'])
    Two_M_Y = (Two['MagTest']['Admin'][f"{j}"]['magnetometer']['y'])
    Two_M_Z = (Two['MagTest']['Admin'][f"{j}"]['magnetometer']['z'])

for k in range(1477, 1589):
    Three_T_X = Three_T_X + [(Bad['MagTest']['Admin'][f"{k}"]['fieldTesla']['x'])]
    Three_T_Y = Three_T_Y + [(Bad['MagTest']['Admin'][f"{k}"]['fieldTesla']['y'])]
    Three_T_Z = Three_T_Z + [(Bad['MagTest']['Admin'][f"{k}"]['fieldTesla']['z'])]
    Three_M_X = (Bad['MagTest']['Admin'][f"{k}"]['magnetometer']['x'])
    Three_M_Y = (Bad['MagTest']['Admin'][f"{k}"]['magnetometer']['y'])
    Three_M_Z = (Bad['MagTest']['Admin'][f"{k}"]['magnetometer']['z'])

#veb = [6,3,7,2]
#zeb = [6,3,7,2]
#Testing Mag Field x
#TestOnex = 1 - spatial.distance.cosine(One_T_X, Two_T_X)
print(One_T_X)
print(Two_T_X)
#print(TestOnex)
### TestTwox = 1 - spatial.distance.cosine(One_T_X, Three_T_X)
#print(TestTwox)
#TestThreex = 1 - spatial.distance.cosine(Two_T_X, Three_T_X)
#print(TestThreex)

#Testing Mag Field y
#TestOney = 1 - spatial.distance.cosine(One_T_Y, Two_T_Y)
#print(TestOney)
#TestTwoy = 1 - spatial.distance.cosine(One_T_Y, Three_T_Y)
#print(TestTwoy)
#TestThreey = 1 - spatial.distance.cosine(Two_T_Y, Three_T_Y)
#print(TestThreey)

#Testing Mag Field z
#TestOnez = 1 - spatial.distance.cosine(One_T_Z, Two_T_Z)
#print(TestOnez)
#TestTwoz = 1 - spatial.distance.cosine(One_T_Z, Three_T_Z)
#print(TestTwoz)
#TestThreez = 1 - spatial.distance.cosine(Two_T_Z, Three_T_Z)
#print(TestThreez)
