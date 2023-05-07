def problems273_c():
    N = int(raw_input())
    A = map(int, raw_input().split())
    A.sort()
    A.append(A[-1]+1)
    ans = [0]*N
    cnt = 1
    for i in range(N):
        if A[i]!=A[i+1]:
            ans[cnt-1]+=1
            cnt = 1
        else:
            cnt+=1
    print '\n'.join(map(str,ans))

if __name__ == '__main__':
    problems273_c()