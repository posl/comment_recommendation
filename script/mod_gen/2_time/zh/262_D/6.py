def count_min_max(a):
    n = len(a)
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if min(a[i],a[j]) == i+1 and max(a[i],a[j]) == j+1:
                count += 1
    return count

if __name__ == '__main__':
    count_min_max()