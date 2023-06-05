def main():
    n,k=map(int,input().split())
    ab=[list(map(int,input().split())) for _ in range(n)]
    ab.sort(key=lambda x:x[0])
    #print(ab)
    money=k
    now=0
    for i in range(n):
        if money>=ab[i][0]-now:
            money+=ab[i][1]
            now=ab[i][0]
        else:
            break
    print(now+money)
main()
