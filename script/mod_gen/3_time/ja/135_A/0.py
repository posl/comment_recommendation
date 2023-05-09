def main():
    A, B = map(int, input().split())
    K = (A + B) // 2
    if abs(A - K) == abs(B - K):
        print(K)
    else:
        print("IMPOSSIBLE")

if __name__ == '__main__':
    main()