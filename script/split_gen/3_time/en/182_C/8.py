def main():
    N = input()
    N = list(map(int, N))
    N = N[::-1]
    mod = 0
    for i in range(len(N)):
        mod += N[i] * pow(10, i, 3)
    mod %= 3
    if mod == 0:
        print(0)
        return
    if mod == 1:
        if 1 in N:
            print(1)
            return
        if len(N) >= 2 and (N[1] + N[2]) % 3 == 1:
            print(2)
            return
        if len(N) >= 3 and (N[2] + N[3]) % 3 == 1:
            print(2)
            return
    if mod == 2:
        if 2 in N:
            print(1)
            return
        if len(N) >= 2 and (N[1] + N[2]) % 3 == 2:
            print(2)
            return
        if len(N) >= 3 and (N[2] + N[3]) % 3 == 2:
            print(2)
            return
    print(-1)
