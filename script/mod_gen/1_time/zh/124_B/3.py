def main():
    N = int(input())
    H_list = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if i == 0:
            count += 1
        else:
            if max(H_list[:i]) <= H_list[i]:
                count += 1
    print(count)

if __name__ == '__main__':
    main()