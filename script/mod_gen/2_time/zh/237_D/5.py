def solve():
    N=int(input())
    S=input()
    ans=[]
    left=0
    right=0
    for i in range(N):
        if S[i]=='L':
            ans.insert(left+1,i+1)
            left+=1
        else:
            ans.append(i+1)
            right+=1
    for i in ans:
        print(i,end=' ')

if __name__ == '__main__':
    solve()