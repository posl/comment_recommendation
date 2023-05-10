def main():
    n = int(input())
    p_list = list(map(int, input().split()))
    p_list_sorted = sorted(p_list)
    count = 0
    for i in range(n):
        if p_list[i] != p_list_sorted[i]:
            count += 1
    if count == 2 or count == 0:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()