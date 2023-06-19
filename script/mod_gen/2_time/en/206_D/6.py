def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 1:
        print(0)
        return
    if N % 2 == 0:
        for i in range(N // 2):
            if A[i] != A[-1 - i]:
                print(1)
                return
        print(0)
        return
    for i in range((N - 1) // 2):
        if A[i] != A[-1 - i]:
            print(1)
            return
    print(0)
    return
main()
