def main():
    a, n = map(int, input().split())
    if a % 2 == 0:
        if n % 2 == 0:
            print(1)
        else:
            print(-1)
    else:
        print(-1)
