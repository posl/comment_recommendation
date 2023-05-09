def main():
    N = int(input())
    P = [int(input()) for _ in range(N)]
    max_p = max(P)
    P.remove(max_p)
    sum_p = sum(P)
    sum_p += max_p / 2
    print(sum_p)

if __name__ == '__main__':
    main()