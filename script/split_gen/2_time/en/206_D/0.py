def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 1:
        print(0)
        return
    if N == 2:
        if A[0] == A[1]:
            print(0)
        else:
            print(1)
        return
    if N % 2 == 0:
        mid = N // 2
    else:
        mid = N // 2 + 1
    if A[:mid] == A[mid:][::-1]:
        print(0)
        return
    else:
        print(1)
        return
