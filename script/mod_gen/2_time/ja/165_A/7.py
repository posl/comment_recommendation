def main():
    K = int(input())
    A, B = map(int, input().split())
    if B // K - A // K > 0:
        print("OK")
    elif A % K == 0:
        print("OK")
    else:
        print("NG")

if __name__ == '__main__':
    main()