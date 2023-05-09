def main():
    N = input()
    k = len(N)
    N = list(map(int, N))
    N.sort(reverse=True)
    N = list(map(str, N))
    N = ''.join(N)
    N = int(N)
    N %= 3
    if N == 0:
        print(0)
        return
    if N == 1:
        if k >= 2:
            print(1)
        else:
            print(-1)
        return
    if N == 2:
        if k >= 2:
            print(1)
        else:
            print(-1)
        return
