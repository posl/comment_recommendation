def main():
    n, k = map(int, input().split())
    d_list = [0] * n
    for _ in range(k):
        d = int(input())
        a_list = list(map(int, input().split()))
        for a in a_list:
            d_list[a - 1] += 1
    print(d_list.count(0))

if __name__ == '__main__':
    main()