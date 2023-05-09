def main():
    A, B, K = [int(x) for x in input().split()]
    d = []
    for i in range(1, max(A, B)+1):
        if A % i == 0 and B % i == 0:
            d.append(i)
    print(d[-K])

if __name__ == '__main__':
    main()