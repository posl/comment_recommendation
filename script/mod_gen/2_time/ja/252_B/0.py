def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if max(A) in B:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()