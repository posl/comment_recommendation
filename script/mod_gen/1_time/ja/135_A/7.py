def main():
    A,B = map(int, input().split())
    if A > B:
        K = (A + B) // 2
        if abs(A - K) == abs(B - K):
            print(K)
        else:
            print("IMPOSSIBLE")
    else:
        K = (A + B) // 2
        if abs(A - K) == abs(B - K):
            print(K)
        else:
            print("IMPOSSIBLE")

if __name__ == '__main__':
    main()