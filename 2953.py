arr=[list(map(int,input().split())) for _ in range(5)] #행이 5개인 행렬 만들기

max=0
max_grd=0
for i in range(5):
    result=0 #항상 0으로 초기화
    for j in range(4):
        result+=arr[i][j]
    if(max_grd<result): #최댓값이 생기면 갱신
        max=i
        max_grd=result

print((max+1),max_grd)
