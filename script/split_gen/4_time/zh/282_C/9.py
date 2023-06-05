def func():
    N = int(input())
    S = input()
    for i in range(0, N, 2):
        if S[i] == "\"":
            S = S[:i] + "." + S[i+1:]
    print(S)
