def count_seq(n, m, k):
    if n == 1:
        return k
    if n == 2:
        return k * (k + 1) // 2
    if n == 3:
        return k * (k + 1) * (k + 2) // 6
    if n == 4:
        return k * (k + 1) * (k + 2) * (k + 3) // 24
    if n == 5:
        return k * (k + 1) * (k + 2) * (k + 3) * (k + 4) // 120
    if n == 6:
        return k * (k + 1) * (k + 2) * (k + 3) * (k + 4) * (k + 5) // 720
    if n == 7:
        return k * (k + 1) * (k + 2) * (k + 3) * (k + 4) * (k + 5) * (k + 6) // 5040
    if n == 8:
        return k * (k + 1) * (k + 2) * (k + 3) * (k + 4) * (k + 5) * (k + 6) * (k + 7) // 40320
    if n == 9:
        return k * (k + 1) * (k + 2) * (k + 3) * (k + 4) * (k + 5) * (k + 6) * (k + 7) * (k + 8) // 362880
    if n == 10:
        return k * (k + 1) * (k + 2) * (k + 3) * (k + 4) * (k + 5) * (k + 6) * (k + 7) * (k + 8) * (k + 9) // 3628800
    if n == 11:
        return k * (k + 1) * (k + 2) * (k + 3) * (k +

if __name__ == '__main__':
    count_seq()