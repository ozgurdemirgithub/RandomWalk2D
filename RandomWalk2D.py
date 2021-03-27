
#2D RandomWalker 
import random,math 
def randomwalk(a,north,west,south,east,N):
    dsum=0
    for j in range(21):
        a=0
        for i in range(N+1):
            a=a+1 #for each step is one unit long
            R = random.randint(1,4)
            if R ==1:
                east=east+1
            if R ==2:
                south=south+1
            if R ==3:
                west=west+1
            if R ==4:
                north=north+1
            if a==N:
                break
        distance=round(math.sqrt((north-south)**2+(west-east)**2),4)#distance from the origin for single random walk
        dsum =+ (distance)**2#take squares of the distances for 20 random walk and sum the results
    
    rmsd=round(math.sqrt(dsum/20),4)#find the avarage value and take the square root for rmsd value
    #RMSD 
    #(S)Take squares.
    #(M) Sum and avarage.
    #(R) Take the square root.

    sqrtN  = round(math.sqrt(N),4)
    percenterror=abs(round(100-( rmsd/sqrtN )*100,4))
    print("Sqrt of N:",sqrtN)
    print("Root Mean Square Distance from the starting point:",rmsd)
    print("%",percenterror,"error")
    return south, east, north ,west, sqrtN 

#extra code to run the walker code for growing number of N's.
def growingnumber(q):#looping 5 times for growing numbers of N
    print("\n","Note that the distance traveled roughly grows like √N. ")
    for i in range(5):
        i=i+1
        q=q+1000
        print("\n",i,".)","N for this walk is",q)
        randomwalk(0,0,0,0,0,q)
        if i==5:
            break       
   
N=int(input("Define the total number of steps (N) for 2D random walk:"))
randomwalk(0,0,0,0,0,N)
growingnumber(N)