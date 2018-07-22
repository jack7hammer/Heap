import sys
def heapify(A, n, r_index):
    
    least = r_index 
   
    left_child_index=2*r_index+1  

  
    right_child_index=2*r_index+2     
 
    if left_child_index < n and A[r_index].lower() > A[left_child_index].lower():
        least = left_child_index
 

    if right_child_index < n and A[least].lower() > A[right_child_index].lower():
        least = right_child_index
 

    if least != r_index:
        A[r_index],A[least] = A[least],A[r_index]  
 
     	
        heapify(A, n, least)
 

def heapSort(A):
    n = len(A)
 
    
    for i in range(n, -1, -1):
        heapify(A, n, i)
    
    for i in range(n-1, 0, -1):  
        A[i], A[0] = A[0], A[i]  
        heapify(A, i, 0)

f1=sys.argv[1]
f2=sys.argv[2]
f=open(f1,"r")
A=[]
i=0
for line in f:
        for word in line.split():
        	A.append(word)
        	i=i+1
print("Input :",A)



heapSort(A)
f.close()

f=open(f2,"w+")

A.reverse()

for words in A:
	f.write(words+" ")
print("output:",A , "\n the writing has been successful")




         
