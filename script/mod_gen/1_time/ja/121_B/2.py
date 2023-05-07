def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        A = list(map(int, input().split()))
        if sum([a*b for a, b in zip(A, B)]) + C > 0:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()