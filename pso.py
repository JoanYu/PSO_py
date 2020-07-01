# imports
import random
import numpy as np
# 
dim=30
def init(popsize,xmin,xmax):
    pop=np.zeros((dim,popsize))
    for i in range(popsize):
        for j in range(dim):
            pop[j][i]=random.uniform(xmin,xmax)
    v=np.zeros((dim,popsize))
    for i in range(popsize):
        for j in range(dim):
            v[j][i]=-1+2*random.random()
    return pop,v

def calfitvalue(pop):
    xn,popn=pop.shape[0],pop.shape[1]
    
    fitvalue=np.zeros((popn,1))
    for i in range(popn):
        fitvalue[i]=sum(pop[:,i]*pop[:,i]-10*np.cos(2*np.pi*pop[:,i])+10)
    gbestvalue=min(fitvalue)
    gbestindex=np.argmin(fitvalue)
    gbest=pop[:,gbestindex]
    return fitvalue,gbestvalue,gbest

def updatepop(pop,v,pbest,gbest,xmin,xmax):
    xn,popn=pop.shape[0],pop.shape[1]
    vmax=10
    omega=0.5
    c1=2
    c2=2
    newv=np.zeros_like(v)
    newpop=np.zeros_like(pop)
    for k in range(popn):
        newv[:,k]=omega*v[:,k]+c1*random.random()*(pbest[:,k]-pop[:,k])+c2*random.random()*(gbest-pop[:,k])
        if np.linalg.norm(newv[:,k])>vmax:
           for i in range(dim):
               newv[i,k]=newv[i,k]*(vmax/np.linalg.norm(newv[:,k]))
        newpop[:,k]=pop[:,k]+newv[:,k]
        for i in range(dim):
            if newpop[i,k]<xmin:
                newpop[i,k]=xmin
            elif newpop[i,k]>xmax:
                newpop[i,k]=xmax
    return newpop,newv

if __name__=='__main__':
    pop,v=init(20,-2,2)
    # print(pop)
    # print(v)
    value,gbestvalue,gbest=calfitvalue(pop)
    # print(value)
    # print(gbestvalue)
    # print(gbest)

