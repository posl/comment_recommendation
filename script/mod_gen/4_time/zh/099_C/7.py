def getLeastCount(n):
    if n == 1:
        return 1
    if n == 6:
        return 1
    if n == 9:
        return 1
    if n == 36:
        return 1
    if n == 81:
        return 1
    if n < 0:
        return 0
    if n < 6:
        return 0
    if n < 9:
        return 0
    if n < 36:
        return getLeastCount(n-6) + 1
    if n < 81:
        return getLeastCount(n-9) + 1
    if n >= 81:
        return min(getLeastCount(n-6) + 1, getLeastCount(n-9) + 1)

if __name__ == '__main__':
    getLeastCount()