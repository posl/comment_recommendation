def solve():
    #n,k,q = map(int,input().split())
    #a = [int(input()) for _ in range(q)]
    n,k,q = 6,5,4
    a = [3,1,3,2]
    score = [k]*n
    for i in range(q):
        score[a[i]-1] -= 1
    for i in range(n):
        if score[i] <= 0:
            print('No')
        else:
            print('Yes')
