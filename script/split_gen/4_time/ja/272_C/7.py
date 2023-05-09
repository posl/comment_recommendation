def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    if a[-1] % 2 == 0:
        print(a[-1])
    elif n == 2:
        print(-1)
    else:
        print(a[-1] + a[-2])
