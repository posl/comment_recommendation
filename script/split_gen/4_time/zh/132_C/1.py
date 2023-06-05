def main():
    N = int(input())
    d = list(map(int, input().split()))
    d.sort()
    if N % 2 == 0:
        print(d[N//2] - d[N//2-1])
    else:
        print(0)
