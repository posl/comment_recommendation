def main():
    a, n = map(int, input().split())
    if n % a != 0:
        print(-1)
        return
    x = n // a
    if x == 1:
        print(1)
        return
    if x % 2 == 0:
        print(2)
        return
    if x % 2 == 1:
        print(3)
        return
