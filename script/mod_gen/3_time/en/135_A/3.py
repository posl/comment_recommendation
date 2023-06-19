def main():
    A, B = map(int, input().split())
    K = (A + B) // 2
    if (A - K) == (B - K):
        print(K)
    else:
        print("IMPOSSIBLE")
main()
