def main():
    K = int(input())
    A, B = map(int, input().split())
    if A % K == 0:
        print("OK")
    elif B % K == 0:
        print("OK")
    elif A % K != 0 and B % K != 0:
        if A // K + 1 <= B // K:
            print("OK")
        else:
            print("NG")
