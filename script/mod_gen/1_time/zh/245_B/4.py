def answer(n, a):
    result = 0
    for i in range(0, n):
        if a[i] == result:
            result += 1
    return result

if __name__ == '__main__':
    answer()