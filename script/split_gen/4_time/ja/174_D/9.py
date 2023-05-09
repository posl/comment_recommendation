def solve():
    N = int(input())
    S = input()
    white = S.count("W")
    red = S.count("R")
    white_count = 0
    red_count = 0
    for i in range(N):
        if S[i] == "W":
            white_count += 1
        else:
            red_count += 1
        if white_count > white - red_count:
            print(red_count)
            return
    print(white_count)
    return
