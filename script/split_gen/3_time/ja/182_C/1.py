def main():
    N = input()
    if int(N) % 3 == 0:
        print(0)
        return
    if len(N) == 1:
        print(-1)
        return
    N = list(map(int, N))
    N.sort()
    N = N[::-1]
    if N[-1] % 2 == 0:
        print(1)
        return
    if sum(N) % 3 == 0:
        print(2)
        return
    print(-1)
    return
