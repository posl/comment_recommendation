def main():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    s = 0
    for i in range(n):
        if v[i] > c[i]:
            s += v[i] - c[i]
    print(s)
