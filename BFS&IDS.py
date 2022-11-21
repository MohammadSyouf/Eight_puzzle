from numpy import *
import numpy as np
import copy 
node1=0
node2=0
node3=0
node4=0
expandedcounter=0
class EightPuzzel:
    def __init__(self,TwoDimArray):
        self.__TwoDimArray=TwoDimArray
    
    def Up(self):
        global node1
        for i in range(3):
            for j in range(3):
                if self.__TwoDimArray[i][j]== 0 and (i==1 or i==2):
                    x=self.__TwoDimArray[i][j]
                    self.__TwoDimArray[i][j]=self.__TwoDimArray[i-1][j]
                    self.__TwoDimArray[i-1][j]=x
                    #print(" i = ",i,"  j = ",j)
                    node1=EightPuzzel(self.__TwoDimArray)
        return node1   

    def Down(self):
        global node2
        counter=0
        for i in range(3):
            for j in range(3):
                if self.__TwoDimArray[i][j]== 0 and (i==0 or i==1 and  counter<1):
                    x=0
                    self.__TwoDimArray[i][j]=self.__TwoDimArray[i+1][j]
                    self.__TwoDimArray[i+1][j]=x
                    #print(" i = ",i,"  j = ",j)
                    node2=EightPuzzel(self.__TwoDimArray)
                    counter+=1
        return node2


    def Right(self):
        counter=0
        global node3
        for i in range(3):
            for j in range(3):
                if self.__TwoDimArray[i][j]== 0 and (j==0 or j==1 and counter<1):
                    x=self.__TwoDimArray[i][j]
                    self.__TwoDimArray[i][j]=self.__TwoDimArray[i][j+1]
                    self.__TwoDimArray[i][j+1]=x
                    #print(" i = ",i,"  j = ",j)
                    node3=EightPuzzel(self.__TwoDimArray)
                    counter+=1
        return node3
        
    def Left(self):
        count=0
        global node4
        for i in range(3):
            for j in range(3):
                if self.__TwoDimArray[i][j]== 0 and (j==1 or j==2) and count==0 :
                    x=self.__TwoDimArray[i][j]
                    self.__TwoDimArray[i][j]=self.__TwoDimArray[i][j-1]
                    self.__TwoDimArray[i][j-1]=x
                    #print(" i = ",i,"  j = ",j)
                    node4=EightPuzzel(self.__TwoDimArray)
                    count+=1
        return node4



    def display(self):
        for i in range(3):
            for j in range(3):
                print(self.__TwoDimArray[i][j],end="  ")
                if j==2:
                    print()

    def equal(self,puzzle):
        count=0
        puzzle=puzzle.getlist()
        for i in range(3):
            for j in range(3):
                if self.__TwoDimArray[i][j]==puzzle[i][j]:
                    count+=1
                    if count ==9:
                        return True
                    return False


    def getlist(self):
        return self.__TwoDimArray

def generateRandomArray():
    TwoDimArr = [0,1,1,2,3,3,4,5,6]
    random.shuffle(TwoDimArr)
    TwoDimArr=np.array(TwoDimArr).reshape(3,3).tolist()
    return TwoDimArr



expanded=[]
def expandNodes(node):
    global expandedcounter
    loci=0
    locj=0
    lst=node.getlist()
    for i in range(3):
            for j in range(3):
                if lst[i][j]==0:
                    loci=i
                    locj=j
                
    #print(" i = ",loci,"  j = ",locj)
    if loci+1<=2:
        count1=0
        a=copy.deepcopy(node)
        a=a.Down()
        for i in expanded:
            if i.getlist()==a:
                count+=1
                #print("here 1")
                break
        if count1==0:
            #print("counter 1 = ",count1)
            expanded.append(a)
            expandedcounter+=1
            #print("down")
                    
    if loci-1>=0:
        count2=0
        b=copy.deepcopy(node)
        b=b.Up()
        for i in expanded:
            if i.getlist()==b.getlist():
                count2+=1
                #print("here 2")
                break
        if count2==0:
            #print("counter 2 = ",count2)
            expanded.append(b)
            expandedcounter+=1

            #print("up")

    if locj+1<=2:
        count3=0
        c=copy.deepcopy(node)
        c=c.Right()
        for i in expanded:
            if i.getlist()==c.getlist():
                count3+=1
                #print("here 3")
                break
        if count3==0:
            #print("counter 3 = ",count3)
            expanded.append(c)
            expandedcounter+=1
            #print("right")
    if locj-1>=0:
        count4=0
        d=copy.deepcopy(node)
        d=d.Left()
        for i in expanded:
            if i.getlist()==d.getlist():
                count4+=1
                #print("here 4")
                break
        if count4==0:
            #print("counter 4 = ",count4)
            expanded.append(d)
            expandedcounter+=1

            #print("left")





visited=[]



def BFS(src ,goal):
    visitedcounter=0
    expanded.append(src)
    expandNodes(src)
    for i in expanded:
        expandNodes(i)
        
        if i.getlist()==goal:
            print("Found")
            print("Expanded Nodes = ",expandedcounter)
            print("Visited Nodes = ",visitedcounter)
            break
        else:
            visitedcounter+=1
            visited.append(i)




def IDS(src,goal):
    global expandedcounter
    
    visitedcounter=0
    visited.append(src)
    expanded.append(src)
    level=0
    count=0
    if level==0 and expanded[0].getlist()==goal:
        expandedcounter+=1
        visitedcounter+=1
        level+=1
        print("Expanded Nodes = ",expandedcounter)
        print("Visited Nodes = ",visitedcounter)
        expanded.pop(0)
    else:
        level+=1
        
    node=0
    
    while level:
        expandNodes(expanded[node])
        for i in expanded:
            if i.getlist()==goal:
                print("Found at Level # ",level)
                print("Expanded Nodes = ",expandedcounter)
                print("Visited Nodes = ",visitedcounter)
                level=-1
                break
            
            else:
                visited.append(i)
                visitedcounter+=1
            
        count+=1
        if len(expanded)==count:
            level+=1
            visitedcounter=0
            for j in expanded:
                del j
        level+=1
        node+=1
        


    
x=generateRandomArray()
obj1=EightPuzzel(x)
goal =[[0,1,1],[2,3,3],[4,5,6]]
print("=======================================")
obj1.display()
print()
print("----------------------------------------------------------------------------")
print("1) Breadth First Search (BFS).")
print("2) Iterative Deepening Search (IDS).")
print("=======================================")
choice=int(input("This matrix is randomly generated 8-Puzzle ,How do you want to solve it ? "))

if choice==1:
    count=1
    print("This Process will take a while please wait ... ")
    BFS(obj1,goal)
    for i in expanded:
        if count<=10:
            print("Step : ",count)
            count+=1
            i.display()
            
    
elif choice==2:
    count=1
    print("This Process will take a while please wait ... ")
    IDS(obj1,goal)
    for i in expanded:
        if count<=10:
            print("Step : ",count)
            i.display()
            count+=1
    






