def main():
    n = int(input())
    seq = {}
    for i in range(n):
        l, *a = map(int, input().split())
        seq[tuple(a)] = 1
    print(len(seq))

if __name__ == '__main__':
    main()