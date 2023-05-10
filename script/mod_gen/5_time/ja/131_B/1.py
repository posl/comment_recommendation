def main():
    n, l = map(int, input().split())
    li = [l+i for i in range(n)]
    print(sum(li[1:]) - li[0])

if __name__ == '__main__':
    main()