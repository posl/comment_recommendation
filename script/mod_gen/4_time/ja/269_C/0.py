def main():
    n = int(input())
    ans = []
    for i in range(2**15):
        x = 0
        for j in range(15):
            if i & (1 << j):
                x = x | (1 << j)
        if x <= n:
            ans.append(x)
    print(*ans, sep='\n')

if __name__ == '__main__':
    main()