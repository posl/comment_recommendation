def main():
    N=int(input())
    s=[]
    t=[]
    for i in range(N):
        a,b=input().split()
        s.append(a)
        t.append(b)
    #print(s)
    #print(t)
    flag=0
    for i in range(N):
        for j in range(N):
            if i!=j:
                if s[i]==s[j] and t[i]==t[j]:
                    flag=1
                    break
    if flag==1:
        print("No")
    else:
        print("Yes")
main()
