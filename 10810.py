N,M=map(int,input().split())

arr=[0]*N
for i in range(M):
    h,j,k=map(int,input().split())
    for l in range((h-1),j):
        arr[l]=k

for i in range(N):
    print(arr[i], end=' ')
