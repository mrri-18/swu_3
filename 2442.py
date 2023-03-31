cnt=int(input())
for i in range(1,cnt+1):
    print(" "*(cnt-i),'*'*(2*i-1),sep='') #뒷 공백을 지워야함
