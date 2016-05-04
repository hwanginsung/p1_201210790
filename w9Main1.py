import math
for i in range(0,len(Local)):
    q=math.sqrt((Local[i][0]-37.602637)**2+(Local[i][1]-126.955254)**2)
    print q

Local2=[0.0324182333418,0.039907346003,0.0375495177333,0.0283059783438,0.0177875672592]
print min(Local2)