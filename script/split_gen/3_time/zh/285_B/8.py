def solve():
    N = int(input())
    S = input()
    for i in range(1,N):
        count = 0
        for j in range(i,N):
            if S[j-i] != S[j]:
                count += 1
        print(count)
