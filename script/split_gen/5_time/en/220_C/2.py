def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    total = sum(A)
    k = (X//total)*N
    X -= (X//total)*total
    for a in A:
        if X < 0:
            break
        X -= a
        k += 1
    print(k)
