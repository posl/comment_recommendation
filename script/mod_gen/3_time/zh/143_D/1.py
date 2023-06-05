def count_triangles(N, L):
    triangles = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i] < L[j] + L[k] and L[j] < L[k] + L[i] and L[k] < L[i] + L[j]:
                    triangles += 1
    return triangles

if __name__ == '__main__':
    count_triangles()