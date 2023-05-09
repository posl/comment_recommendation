def main():
    N = int(input())
    max_bit = 0
    for i in range(60):
        if N & (1 << i):
            max_bit = i
    ans = []
    for i in range(1 << (max_bit + 1)):
        if i & N == i:
            ans.append(i)
    print(*ans, sep='\n')

if __name__ == '__main__':
    main()