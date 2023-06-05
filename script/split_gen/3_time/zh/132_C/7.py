def main():
    n = int(input())
    d = list(map(int, input().split()))
    d.sort()
    a = d[:n//2]
    b = d[n//2:]
    print(b[0] - a[-1])
