def main():
    K = int(input())
    A, B = map(int, input().split())
    if A % K == 0:
        print("OK")
    elif B % K == 0:
        print("OK")
    elif A < K and B < K:
        print("NG")
    elif A < K and B > K:
        print("OK")
    elif A > K and B < K:
        print("NG")
    elif A > K and B > K:
        if (A // K) < (B // K):
            print("OK")
        else:
            print("NG")
main()
