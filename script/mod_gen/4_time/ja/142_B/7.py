def main():
    N, K = map(int, input().split())
    h_list = list(map(int, input().split()))
    count = 0
    for h in h_list:
        if h >= K:
            count += 1
    print(count)
main()

if __name__ == '__main__':
    main()