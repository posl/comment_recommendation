def find_kth_permutation(n, k, permutation):
    if n == 0:
        return permutation
    index, fac = 0, factorial(n - 1)
    while k > fac:
        index += 1
        k -= fac
    permutation.append(index + 1)
    return find_kth_permutation(n - 1, k, permutation)
