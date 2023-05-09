def main():
    n = int(input())
    s, t = input().split()
    print(''.join([i + j for i, j in zip(s, t)]))

if __name__ == '__main__':
    main()