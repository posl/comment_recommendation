def main():
    N = int(input())
    if N % 3 == 0:
        print(0)
        return
    N = str(N)
    if len(N) == 1:
        print(-1)
        return
    if N.count('0') >= 1:
        print(1)
        return
    if len(N) == 2:
        print(-1)
        return
    if (int(N[0]) + int(N[1]) + int(N[2])) % 3 == 0:
        print(2)
        return
    if (int(N[1]) + int(N[2]) + int(N[3])) % 3 == 0:
        print(2)
        return
    print(-1)
    return
