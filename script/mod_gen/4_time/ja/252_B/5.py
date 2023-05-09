def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    max_a = max(A)
    if max_a in B:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()