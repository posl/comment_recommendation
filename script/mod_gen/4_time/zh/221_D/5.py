def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    days = []
    for i in range(N):
        for j in range(B[i]):
            days.append(A[i]+j)
    #print(days)
    days.sort()
    #print(days)
    count = 0
    ans = []
    for i in range(len(days)-1):
        count += 1
        if days[i] != days[i+1]:
            ans.append(count)
            count = 0
    ans.append(count+1)
    #print(ans)
    for i in range(N):
        print(ans[i],end=' ')

if __name__ == '__main__':
    main()