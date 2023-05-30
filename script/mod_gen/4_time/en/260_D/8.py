def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    #print(n,k,p)
    ans = [-1 for i in range(n)]
    #print(ans)
    stack = []
    for i in range(n):
        #print("i",i)
        while stack and p[stack[-1]] > p[i]:
            #print("stack",stack)
            #print("p[stack[-1]]",p[stack[-1]])
            #print("p[i]",p[i])
            ans[stack.pop()] = i + 1
            #print("ans",ans)
        stack.append(i)
        #print("stack",stack)
    print(*ans,sep="\n")
main()
