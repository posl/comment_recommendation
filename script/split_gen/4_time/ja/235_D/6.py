def main():
    a, N = map(int, input().split())
    if N < 10:
        if N % a == 0:
            print(1)
        else:
            print(-1)
        return
    if a == 2:
        print(len(bin(N)) - 3)
        return
    if a == 3:
        print(len(oct(N)) - 2)
        return
    if a == 5:
        print(len(hex(N)) - 2)
        return
    if a == 6:
        print(len(hex(N)) - 2)
        return
    if a == 7:
        print(len(oct(N)) - 2)
        return
    if a == 8:
        print(len(bin(N)) - 3)
        return
    if a == 9:
        print(len(oct(N)) - 2)
        return
    print(-1)
