def solution(n):
    if n == 0:
        return 0
    elif n < 6:
        return n
    else:
        min_num = n
        for i in range(1, 6):
            if n >= 6 ** i:
                min_num = min(min_num, solution(n - 6 ** i) + 1)
            if n >= 9 ** i:
                min_num = min(min_num, solution(n - 9 ** i) + 1)
        return min_num

if __name__ == '__main__':
    solution()