def main():
    W = int(input())
    if W % 2 == 0:
        ans = [W // 2, W // 2]
    else:
        ans = [W // 2, W // 2 + 1]
    print(len(ans))
    print(*ans)

if __name__ == '__main__':
    main()