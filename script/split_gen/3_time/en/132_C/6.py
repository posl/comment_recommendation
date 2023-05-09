def main():
    #input
    N = int(input())
    d = list(map(int, input().split()))
    #count
    d.sort()
    print(d[N//2] - d[N//2-1])
