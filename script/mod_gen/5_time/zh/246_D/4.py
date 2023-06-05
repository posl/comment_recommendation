def calc(N):
    if N == 0:
        return 0
    if N == 1:
        return 1
    for i in range(1, 100):
        if i**3 > N:
            break
        for j in range(i, 100):
            if i**3 + i**2*j + i*j**2 + j**3 > N:
                break
            for k in range(j, 100):
                if i**3 + i**2*j + i*j**2 + j**3 + j**2*k + j*k**2 + k**3 > N:
                    break
                if i**3 + i**2*j + i*j**2 + j**3 + j**2*k + j*k**2 + k**3 == N:
                    return i**3 + i**2*j + i*j**2 + j**3 + j**2*k + j*k**2 + k**3
    return -1

if __name__ == '__main__':
    calc()