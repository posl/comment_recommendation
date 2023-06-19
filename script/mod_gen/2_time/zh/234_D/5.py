def max_k(a,k):
    max = 0
    for i in range(k):
        if a[i] > max:
            max = a[i]
    return max

if __name__ == '__main__':
    max_k()