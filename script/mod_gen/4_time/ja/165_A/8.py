def main():
    K = int(input())
    A, B = map(int, input().split())
    if A % K == 0 or B % K == 0:
        print("OK")
        exit()
    else:
        print("NG")
        exit()

if __name__ == '__main__':
    main()