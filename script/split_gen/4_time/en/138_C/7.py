def main():
    n = int(input())
    vl = list(map(int, input().split()))
    vl.sort()
    for i in range(1, n):
        vl[i] = (vl[i] + vl[i-1]) / 2
    print(vl[n-1])
