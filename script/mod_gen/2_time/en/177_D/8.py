def main():
    n,m=map(int,input().split())
    e=[[] for i in range(n)]
    for i in range(m):
        a,b=map(int,input().split())
        a-=1
        b-=1
        e[a].append(b)
        e[b].append(a)
    def dfs(v):
        if v in s:
            return
        s.add(v)
        for u in e[v]:
            dfs(u)
    s=set()
    cnt=0
    for i in range(n):
        if i not in s:
            dfs(i)
            cnt+=1
    print(cnt)
main()
You can find the problem here.
I am a beginner in competitive programming. I am trying to solve this problem. I am using python. I have written the following code. But I am getting wrong answer. Can you please tell me where I am going wrong?

if __name__ == '__main__':
    main()