def count_generation(n, parent):
    count = 0
    for i in range(n):
        p = parent[i]
        while p != -1:
            count += 1
            p = parent[p-1]
    return count

if __name__ == '__main__':
    count_generation()