def cut_rod(L):
    if L == 0:
        return 1
    if L < 0:
        return 0
    return cut_rod(L-1) + cut_rod(L-2) + cut_rod(L-3) + cut_rod(L-4) + cut_rod(L-5) + cut_rod(L-6) + cut_rod(L-7) + cut_rod(L-8) + cut_rod(L-9) + cut_rod(L-10) + cut_rod(L-11)

if __name__ == '__main__':
    cut_rod()