def main():
    n = int(input())
    h_list = list(map(int, input().split()))
    count = 0
    max = 0
    for i in range(n):
        if h_list[i] >= max:
            max = h_list[i]
            count += 1
    print(count)

if __name__ == '__main__':
    main()