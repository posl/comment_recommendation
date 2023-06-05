def solve():
    #请在这里编写代码
    N = int(input())
    S = input()
    S = list(S)
    for i in range(1, N + 1):
        if i % 2 == 0:
            if S[i - 1] == '"':
                S[i - 1] = '.'
    print(''.join(S))
