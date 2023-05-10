def solve():
    N = int(input())
    S = input()
    res = 0
    for i in range(N-2):
        if S[i:i+3] == "ABC":
            res += 1
    print(res)
