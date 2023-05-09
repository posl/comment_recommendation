def solve():
    N = int(input())
    P = [int(x) for x in input().split()]
    #print(N, P)
    count = 0
    for i in range(N):
        if i == P[P[i]]:
            count += 1
    #print(count)
    if count == N:
        print(N)
    else:
        print(count-1)
