def main():
    a, n = map(int, input().split())
    if n == 1:
        print(0)
        return
    if a == 2:
        print(len(bin(n)) - 3)
        return
    if a == 10:
        print(len(str(n)) - 1)
        return
    if n % a == 0:
        print(-1)
        return
    if n % a == 1:
        print(len(str(n)) - 1)
        return
    if n % a == 2:
        print(len(str(n)) - 1)
        return
    if n % a == 3:
        print(len(str(n)) - 1)
        return
    if n % a == 4:
        print(len(str(n)) - 1)
        return
    if n % a == 5:
        print(len(str(n)) - 1)
        return
    if n % a == 6:
        print(len(str(n)) - 1)
        return
    if n % a == 7:
        print(len(str(n)) - 1)
        return
    if n % a == 8:
        print(len(str(n)) - 1)
        return
    if n % a == 9:
        print(len(str(n)) - 1)
        return
