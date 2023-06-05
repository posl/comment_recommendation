def solve():
    P = list(map(int, input().split()))
    S = [chr(i+96) for i in P]
    print(''.join(S))
