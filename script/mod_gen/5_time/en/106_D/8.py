def find_trains (L, R, p, q):
    trains = 0
    for i in range(len(L)):
        if L[i] >= p and R[i] <= q:
            trains += 1
    return trains

if __name__ == '__main__':
    find_trains()