def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = sorted(a)
    k1 = k//n
    k2 = k%n
    for i in range(n):
        if i < k2:
            print(k1+1)
        else:
            print(k1)
