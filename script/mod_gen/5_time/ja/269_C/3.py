def main():
    N = int(input())
    ans = []
    for i in range(0, 2**15):
        if i & N == i:
            ans.append(i)
    print(*ans, sep='\n')

if __name__ == '__main__':
    main()