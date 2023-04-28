word=list(input()) #문장을 입력받음
cnt=1
for i in range(1,(len(word)-1)): #맨 앞에 공백, 맨 뒤에 공백이 있는 경우 제외
    if(word[i]==" "): 
         cnt+=1
if(word[0]==" " and len(word)==1): #word에 " "만 저장된 경우
     print(0)
else:
     print(cnt)