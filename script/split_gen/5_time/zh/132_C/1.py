def main():
    N = int(input())
    d = list(map(int, input().split()))
    d.sort()
    if N == 2:
        print(d[1] - d[0])
    else:
        print(d[N//2] - d[N//2-1])
