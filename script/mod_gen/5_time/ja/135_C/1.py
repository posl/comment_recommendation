def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if a_list[i] <= b_list[i]:
            count += a_list[i]
            b_list[i] -= a_list[i]
            if a_list[i+1] <= b_list[i]:
                count += a_list[i+1]
                a_list[i+1] = 0
            else:
                count += b_list[i]
                a_list[i+1] -= b_list[i]
        else:
            count += b_list[i]
    print(count)

if __name__ == '__main__':
    main()