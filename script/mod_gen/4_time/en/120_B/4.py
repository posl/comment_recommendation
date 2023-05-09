def main():
    A, B, K = map(int, input().split())
    c = 0
    for i in range(1, max(A, B) + 1):
        if A % i == 0 and B % i == 0:
            c += 1
            if c == K:
                print(i)
                break
main()

if __name__ == '__main__':
    main()