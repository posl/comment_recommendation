def main():
    A, B, K = map(int, input().split())
    if A >= B:
        print(0)
        return
    if K <= A:
        print(A - K)
        return
    if K <= A + B:
        print(0)
        return
    print(A - K + B)
