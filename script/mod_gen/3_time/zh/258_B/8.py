def get_max_num(n):
    if n == 1:
        return int(input())
    else:
        num_list = []
        for i in range(n):
            num_list.append(list(map(int, input().split())))
        max_num = 0
        for i in range(n):
            for j in range(n):
                max_num = max(max_num, num_list[i][j])
        return max_num

if __name__ == '__main__':
    get_max_num()