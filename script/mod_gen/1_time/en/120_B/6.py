def main():
    A, B, K = map(int, input().split())
    cnt = 0
    for i in range(1, min(A, B) + 1):
        if A % i == 0 and B % i == 0:
            cnt += 1
        if cnt == K:
            print(i)
            break
main()

if __name__ == '__main__':
    main()