def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[-1] % 2 == 0:
        print(a[-1])
    elif a[-2] % 2 == 0:
        print(a[-2])
    else:
        print(-1)
