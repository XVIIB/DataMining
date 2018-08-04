import math

def euclideanDistance(x,y):
    return math.sqrt(sum([(a-b)**2 for (a,b) in zip (x,y)]))

def partition(points,k,means,d=euclideanDistance):
    thePartition=[[] for _ in means]
    indices = range(k)
    
    for x in points:
        closestIndex = min(indices, key=lambda index: d(x,means[index]))
        thePartition[closestIndex].append(x)
    return thePartition

def mean(points):
    n = len(points)
    return tuple(float(sum(x))/ n for x in zip(*points))

def kMeans(points,k,initialMeans,d=euclideanDistance):
    oldPartition=[]
    newPartition=partition(points,k,initialMeans,d)
    
    while oldPartition != newPartition:
        oldPartition = newPartition
        newMeans = [mean(S) for S in oldPartition]
        newPartition = partition(points,k,newMeans,d)
        
    return newPartition

def importData():
    f=lambda name,b,d: [name,float(b),float(d)]
    
    with open('data/birth-death-rates.csv','r') as inputFile:
        return [f(*line.strip().split('\t'))for line in inputFile]
    
if __name__ =="__main__":
    L=[x[1:] for x in importData()]
    
    import matplotlib.pyplot as plt
    
    import random
    k=3
    
    partition=kMeans(L,k,random.sample(L,k))
    plt.scatter(*zip(*partition[0]), c='b')
    plt.scatter(*zip(*partition[1]), c='r')
    plt.scatter(*zip(*partition[2]), c='g')
    plt.show()