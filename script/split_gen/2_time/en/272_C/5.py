def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[-1] % 2 == 1:
        a.pop()
    if len(a) % 2 == 1:
        a.pop()
    if len(a) == 0:
        print(-1)
    else:
        print(a[-1] + a[-2])
