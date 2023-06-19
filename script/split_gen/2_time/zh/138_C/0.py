def main():
    n = int(input())
    v = list(map(int, input().split()))
    v.sort()
    print(v[0])
    for i in range(1, n):
        print(v[i])
        v[i] = (v[i] + v[i - 1]) / 2
    print(v[n - 1])
