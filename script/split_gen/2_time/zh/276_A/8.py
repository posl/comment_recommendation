def solve():
    S = input()
    if 'a' in S:
        print(S.rindex('a') + 1)
    else:
        print(-1)
