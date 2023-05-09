def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    while len(a) > 1:
        if a[-1] > a[-2]:
            a[-1] = a[-1] % a[-2]
            a.sort()
        else:
            a.pop(-1)
    print(a[0])
