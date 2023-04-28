N,M=map(int,input().split()) 
arr=['']*N
for i in range(N):
    arr[i]=(i+1)

for k in range(M):
    i,j=map(int,input().split())
    tmp=arr[i-1]
    arr[i-1]=arr[j-1]
    arr[j-1]=tmp
for i in range(N):
    print(arr[i],end=' ') 


