def main():
    N = int(input())
    d = list(map(int, input().split()))
    d.sort()
    if d[N//2-1] == d[N//2]:
        print(0)
    else:
        print(d[N//2]-d[N//2-1])
