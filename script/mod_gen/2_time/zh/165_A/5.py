def main():
    K = int(input())
    A,B = map(int,input().split())
    if A % K == 0:
        print("OK")
    elif A // K != B // K:
        print("OK")
    else:
        print("NG")

if __name__ == '__main__':
    main()