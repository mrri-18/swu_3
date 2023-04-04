#최대, 최소

cnt=int(input())
arr=list(map(int,input().split())) #리스트에 한 줄 입력받기
max=arr[0]
min=arr[0]
for i in range(cnt):
    if(max<arr[i]): max=arr[i]
    if(min>arr[i]): min=arr[i]
print(min, max)