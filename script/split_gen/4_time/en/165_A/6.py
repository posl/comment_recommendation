def solve():
    K = int(input())
    A, B = map(int, input().split())
    if A % K == 0 or B % K == 0:
        print("OK")
        return
    if A // K != B // K:
        print("OK")
        return
    print("NG")
