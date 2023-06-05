def get_num_triangle(N, L):
    L.sort()
    num_triangle = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i] != L[j] and L[j] != L[k] and L[k] != L[i]:
                    if L[i] + L[j] > L[k]:
                        num_triangle += 1
    return num_triangle

if __name__ == '__main__':
    get_num_triangle()