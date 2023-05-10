def main():
    n = int(input())
    p_list = list(map(int, input().split()))
    count = 0
    for i in range(1, n-1):
        if p_list[i-1] < p_list[i] < p_list[i+1] or p_list[i-1] > p_list[i] > p_list[i+1]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()