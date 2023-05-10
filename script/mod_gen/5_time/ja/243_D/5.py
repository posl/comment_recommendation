def solve():
    N, X = map(int, input().split())
    S = input()
    answer = X
    for i in range(N):
        if S[i] == "U":
            answer //= 2
        elif S[i] == "L":
            answer = answer * 2 - 1
        else:
            answer = answer * 2 + 1
    print(answer)

if __name__ == '__main__':
    solve()