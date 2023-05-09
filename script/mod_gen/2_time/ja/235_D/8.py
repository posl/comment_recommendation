def main():
    a, N = map(int, input().split())
    if N % a == 0:
        print(-1)
        return
    # a が N の約数になるまでの回数
    count = 0
    while N % a != 0:
        N = int(str(N)[1:] + str(N)[0])
        count += 1
    print(count)

if __name__ == '__main__':
    main()