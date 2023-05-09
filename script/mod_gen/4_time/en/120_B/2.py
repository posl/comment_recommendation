def main():
    A, B, K = map(int, input().split())
    common = []
    for i in range(1, min(A, B) + 1):
        if A % i == 0 and B % i == 0:
            common.append(i)
    print(common[-K])

if __name__ == '__main__':
    main()