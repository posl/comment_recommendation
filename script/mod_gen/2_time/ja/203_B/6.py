def main():
    N, K = map(int, input().split())
    print(sum([int(str(i) + str(j) + str(k)) for i in range(1, N+1) for j in range(1, K+1) for k in range(1, K+1)]))

if __name__ == '__main__':
    main()