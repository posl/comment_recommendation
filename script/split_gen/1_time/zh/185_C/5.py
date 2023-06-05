def cut_rod(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return cut_rod(n - 1) + cut_rod(n - 2) + cut_rod(n - 3) + cut_rod(n - 4) + cut_rod(n - 5) + cut_rod(n - 6)
