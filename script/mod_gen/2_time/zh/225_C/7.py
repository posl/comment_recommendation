def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n-1)]
    ab = sorted(ab, key=lambda x: x[1])
    ab = sorted(ab, key=lambda x: x[0])
    max_num = max([i[1] for i in ab])
    if ab[-1][1] == max_num:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()