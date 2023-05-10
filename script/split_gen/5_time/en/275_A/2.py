def main():
    n = int(input())
    h = list(map(int, input().split()))
    h.sort()
    print(h[n-1])
