def main():
    N = int(input())
    d = [int(i) for i in input().split()]
    d.sort()
    print(d[N//2] - d[N//2-1])
