def main():
    n = int(input())
    h_list = list(map(int, input().split()))
    count = 0
    max_height = 0
    for h in h_list:
        if h >= max_height:
            count += 1
            max_height = h
    print(count)

if __name__ == '__main__':
    main()