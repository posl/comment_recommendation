def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    mul = []
    for i in range(n-1):
        for j in range(i+1, n):
            mul.append(a[i]*a[j])
    mul.sort()
    print(mul[k-1])
