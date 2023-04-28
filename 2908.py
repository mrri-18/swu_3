num1,num2=list(input().split()) #문자열 입력 받음, 공백을 기준으로 분리

i=2

while(1):
    if(num1[i]>num2[i]): #문자열끼리 비교, int/float/bool 등은 인덱싱, 슬라이싱 등 불가
        for j in range(2,-1,-1):
            print(num1[j],end='')
        break
    elif(num1[i]<num2[i]):
        for j in range(2,-1,-1):
            print(num2[j],end='')
        break
    i-=1


