def find_num_of_triangles(n, edges):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if edges[i][j] == 1:
                for k in range(j+1, n):
                    if edges[i][k] == 1 and edges[j][k] == 1:
                        count += 1
    return count

if __name__ == '__main__':
    find_num_of_triangles()