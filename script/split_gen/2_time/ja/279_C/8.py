def solve():
    H,W = map(int,input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    S = list(map(lambda x: list(x), S))
    T = list(map(lambda x: list(x), T))
    S = list(map(lambda x: list(map(lambda y: 1 if y == "#" else 0, x)), S))
    T = list(map(lambda x: list(map(lambda y: 1 if y == "#" else 0, x)), T))
    S = list(map(lambda x: list(map(lambda y: y%2, x)), S))
    T = list(map(lambda x: list(map(lambda y: y%2, x)), T))
    A = list(map(lambda x: x[0], S))
    B = list(map(lambda x: x[0], T))
    S = list(map(lambda x: x[1:], S))
    T = list(map(lambda x: x[1:], T))
    S = list(map(lambda x: sum(x), S))
    T = list(map(lambda x: sum(x), T))
    S = list(map(lambda x: x%2, S))
    T = list(map(lambda x: x%2, T))
    if A == B and S == T:
        print("Yes")
    else:
        print("No")
