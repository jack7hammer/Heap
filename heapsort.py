
def heapify(A, n, r_index):
   
    least = r_index 
   
    left_child_index=2*r_index+1  

  
    right_child_index=2*r_index+2     
 
    if left_child_index < n and A[r_index] > A[left_child_index]:
        least = left_child_index
 

    if right_child_index < n and A[least] > A[right_child_index]:
        least = right_child_index
 

    if least != r_index:
        A[r_index],A[least] = A[least],A[r_index]  
 
     
        heapify(A, n, least)
 

def heapSort(A):
    n = len(A)
 
    
    for i in range(n, -1, -1):
        heapify(A, n, i)
    print("\nthe heap is : ",A)
    
    for i in range(n-1, 0, -1):  
        A[i], A[0] = A[0], A[i]  
        heapify(A, i, 0)         



print("give the array seperated by spaces")
x=input().split()
A=[int(num) for num in x]

heapSort(A)
n = len(A)
print("\nSorted list")
for i in range(n-1,-1,-1):
    print(A[i])