def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    p.insert(0,0)
    stack = []
    ans = [-1]*(n+1)
    for i in range(1,n+1):
        while stack and p[i] <= p[stack[-1]]:
            stack.pop()
        if stack:
            ans[i] = stack[-1]
        stack.append(i)
    for i in range(n):
        print(ans[i+1])
