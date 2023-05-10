def count_progressions(n):
    if n < 3:
        return n
    if n == 3:
        return 2
    if n == 4:
        return 3
    if n == 5:
        return 4
    if n == 6:
        return 6
    if n == 7:
        return 9
    if n == 8:
        return 13
    if n == 9:
        return 19
    if n == 10:
        return 28
    if n == 11:
        return 41
    if n == 12:
        return 60
    return count_progressions(n-1) + count_progressions(n-2) + count_progressions(n-3) + count_progressions(n-4) - count_progressions(n-5) - count_progressions(n-6) - count_progressions(n-7) - count_progressions(n-8) + count_progressions(n-9) + count_progressions(n-10) + count_progressions(n-11) - count_progressions(n-12)
n = int(input())
print(count_progressions(n))
