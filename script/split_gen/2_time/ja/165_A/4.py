def main():
    K = int(input())
    A, B = map(int, input().split())
    if B // K - A // K == 0:
        if A % K == 0:
            print("OK")
        else:
            print("NG")
    else:
        print("OK")
