def judge(n):
    for i in range(0, 26):
        for j in range(0, 15):
            if (i * 4 + j * 7) == n:
                return True
    return False
n = int(input())

if __name__ == '__main__':
    judge()