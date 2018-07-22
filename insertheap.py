def addheap(A, n, r_index):
    
    least = r_index
    p_index=0
    
    if r_index%2!=0:
        p_index=int((r_index-1)/2)
    if r_index%2==0:
        p_index=int((r_index-2)/2)

    if A[p_index]>A[r_index] and p_index>=0:
     A[p_index],A[r_index]=A[r_index],A[p_index]
    
    least=p_index

    if least!=r_index:

        addheap(A,n,least)


def insert1(A,x):
    n=len(A)
    A.append(x)
    
    if n>0:
        addheap(A, n+1, n)
    print("this is the heap",A)


A=[]
y=int(input("how many numbers do you want to insert?"))
for i in range(0 , y):
    x=int(input("Insert:"))
    insert1(A,x)


