def main():
    n = int(input())
    a = list(map(int, input().split()))
    c = [0] * (max(a)+1)
    for i in range(n):
        c[a[i]] += 1
    s = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] * a[j] <= max(a):
                s += c[a[i]*a[j]]
    print(s)
