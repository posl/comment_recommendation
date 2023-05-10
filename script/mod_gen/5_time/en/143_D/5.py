def count_triangles(L):
    L.sort()
    count = 0
    for i in range(len(L)-2):
        for j in range(i+1, len(L)-1):
            for k in range(j+1, len(L)):
                if L[i] + L[j] > L[k]:
                    count += 1
                else:
                    break
    return count

if __name__ == '__main__':
    count_triangles()