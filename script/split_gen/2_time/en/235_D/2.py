def main():
    a, n = map(int, input().split())
    if n < a:
        print(-1)
        return
    if n == a:
        print(1)
        return
    if n % a == 0:
        print(1)
        return
    if a % 2 == 0:
        if n % 2 == 1:
            print(-1)
            return
        if n % 4 == 0:
            print(2)
            return
        if n % 4 == 2:
            print(3)
            return
    if a % 2 == 1:
        if n % 2 == 0:
            print(-1)
            return
        if n % 4 == 1:
            print(2)
            return
        if n % 4 == 3:
            print(3)
            return
    return
