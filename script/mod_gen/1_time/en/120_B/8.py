def main():
    A, B, K = map(int, input().split())
    divs = []
    for i in range(1, min(A, B)+1):
        if A % i == 0 and B % i == 0:
            divs.append(i)
    print(divs[-K])

if __name__ == '__main__':
    main()