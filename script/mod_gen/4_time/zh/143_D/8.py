def calc_triangle_num(L):
    L.sort()
    num = 0
    for i in range(0, len(L) - 2):
        for j in range(i + 1, len(L) - 1):
            for k in range(j + 1, len(L)):
                if L[i] + L[j] > L[k]:
                    num += 1
                else:
                    break
    return num

if __name__ == '__main__':
    calc_triangle_num()