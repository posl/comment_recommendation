def count_seq(N, C):
    mod = 10**9 + 7
    C.sort()
    count = 1
    for i in range(N):
        count *= C[i] - i
        count %= mod
    return count

if __name__ == '__main__':
    count_seq()