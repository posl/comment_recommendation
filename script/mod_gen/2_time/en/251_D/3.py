def main():
    W = int(input())
    ans = []
    for i in range(1,W+1):
        ans.append(i)
        if len(ans) == 300:
            break
    print(len(ans))
    print(*ans)

if __name__ == '__main__':
    main()