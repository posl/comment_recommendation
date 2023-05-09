def check_permutation(n, a):
    a.sort()
    for i in range(n):
        if a[i] != i+1:
            return "No"
    return "Yes"

if __name__ == '__main__':
    check_permutation()