# imports
import pso
import numpy as np
import matplotlib.pyplot as plt

#
popsize=200
xmin=-5.12
xmax=5.12
degree=2000

pop,v=pso.init(popsize,xmin,xmax)
value,gbest_value,gbest=pso.calfitvalue(pop)
pbest=pop

# plt.figure()

# plt.ion()
xx=[]
ymax=[]
ymin=[]
ymean=[]
for i in range(degree):
    plt.cla()

    xx.append(i)

    newpop,newv=pso.updatepop(pop,v,pbest,gbest,xmin,xmax)
    v=newv
    pop=newpop
    newvalue,newgbest_value,newgbest=pso.calfitvalue(newpop)

    for j in range(popsize):
        if newvalue[j]<value[j]:
            pbest[:,j]=newpop[:,j]
    
    if newgbest_value<gbest_value:
        gbest_value=newgbest_value
        gbest=newgbest
    ymin.append(gbest_value)
    print(np.min(gbest_value))
    plt.plot(xx,ymin,'r-')
    plt.pause(0.05)

plt.ioff()


plt.show()
# print(ymin)