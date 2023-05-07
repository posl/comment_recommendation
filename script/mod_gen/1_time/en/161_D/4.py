def lunlun(n, k):
    if k == 1:
        return n
    else:
        if n % 10 == 9:
            return lunlun(n * 10 + n % 10 - 1, k - 1)
        elif n % 10 == 0:
            return lunlun(n * 10 + n % 10 + 1, k - 1)
        else:
            return min(lunlun(n * 10 + n % 10 - 1, k - 1), lunlun(n * 10 + n % 10 + 1, k - 1))
k = int(input())
print(lunlun(0, k))

if __name__ == '__main__':
    lunlun()