def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    min_A = min([min(a) for a in A])
    print(sum([sum(a) for a in A]) - min_A * H * W)

if __name__ == '__main__':
    main()