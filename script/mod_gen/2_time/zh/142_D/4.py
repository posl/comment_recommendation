def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    order = [0 for _ in range(n)]
    for i in range(n):
        order[a_list[i] - 1] = i + 1
    print(' '.join(map(str, order)))

if __name__ == '__main__':
    main()