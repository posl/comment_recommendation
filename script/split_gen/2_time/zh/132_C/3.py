def main():
    N = int(input())
    d = list(map(int, input().split()))
    d.sort()
    # print(d)
    # print(d[N//2-1])
    # print(d[N//2])
    if d[N//2-1] == d[N//2]:
        print(0)
    else:
        print(d[N//2]-d[N//2-1])
