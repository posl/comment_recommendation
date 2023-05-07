def main():
    K = int(input())
    A, B = map(int, input().split())
    if (B // K) - (A // K) >= 1 or A % K == 0:
        print("OK")
    else:
        print("NG")
