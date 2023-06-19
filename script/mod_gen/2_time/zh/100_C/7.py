def solution(n, a_list):
    count = 0
    while True:
        flag = False
        for i in range(0, n):
            if a_list[i] % 2 == 0:
                a_list[i] = a_list[i] / 2
                flag = True
        if flag:
            count += 1
        else:
            break
    return count

if __name__ == '__main__':
    solution()