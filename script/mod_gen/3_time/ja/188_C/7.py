def binary_search(l, r, A):
    if r - l == 1:
        return r
    else:
        m = (l + r) // 2
        if A[m] > A[m + 1]:
            return binary_search(l, m, A)
        else:
            return binary_search(m, r, A)
N = int(input())
A = list(map(int, input().split()))
print(binary_search(0, 2**N - 1, A))

if __name__ == '__main__':
    binary_search()