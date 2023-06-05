def solution(k):
    if k % 2 == 0:
        return 2
    elif k % 5 == 0:
        return 5
    else:
        return 1

if __name__ == '__main__':
    solution()