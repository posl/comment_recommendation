def main():
    N = int(input())
    A = list(map(int, input().split()))
    if 0 in A:
        print(0)
    else:
        product = 1
        for i in range(N):
            product *= A[i]
            if product > 10**18:
                print(-1)
                return
        print(product)
