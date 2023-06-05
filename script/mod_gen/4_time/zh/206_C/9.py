def count_pairs(n, a):
    # Write your code here
    # To print results to the standard output you can use print
    total = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] != a[j]:
                total += 1
    return total

if __name__ == '__main__':
    count_pairs()