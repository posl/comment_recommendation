def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    if N == K:
        print("Yes")
        return
    if K == 1:
        if A == sorted(A):
            print("Yes")
        else:
            print("No")
        return
    if K % 2 == 0:
        if A == sorted(A):
            print("Yes")
        else:
            print("No")
        return
    if N % 2 == 0:
        if A == sorted(A):
            print("Yes")
        else:
            print("No")
        return
    if A == sorted(A):
        print("Yes")
    else:
        print("No")
    return

if __name__ == '__main__':
    main()