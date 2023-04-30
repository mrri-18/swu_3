word=list(input())
ex=[-1]*26
for j in range(len(word)):
    for i in range(97,123):
        if(word[j]==chr(i) and ex[(i-97)]==-1): #해당 철자와 알파벳 아스키코드를 비교, 이미 등장하지 않았다면
            ex[(i-97)]=j #새로 추가, 해당 인덱스를 대입

for i in range(len(ex)):
    print(ex[i],end=' ')