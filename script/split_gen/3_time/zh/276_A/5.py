def solve():
    S = input()
    if 'a' in S:
        print(S.rfind('a')+1)
    else:
        print(-1)
