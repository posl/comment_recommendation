def main():
    N, D = map(int, input().split())
    count = 0
    for i in range(1, N+1):
        if i % (2*D+1) == 0:
            count += 1
    print(count)

if __name__ == '__main__':
    main()