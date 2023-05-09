def main():
    n = int(input())
    v = list(map(int, input().split()))
    v.sort()
    for i in range(n-1):
        v[0] = (v[0] + v[1]) / 2
        v.sort()
    print(v[0])
