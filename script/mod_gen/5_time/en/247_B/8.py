def main():
    n = int(input())
    name = [input().split() for _ in range(n)]
    name = [i[0] + i[1] for i in name]
    if len(name) == len(set(name)):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()