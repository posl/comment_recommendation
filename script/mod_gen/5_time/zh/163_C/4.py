def get_subordinate_num(N, A):
    subordinate_num = [0] * N
    for i in range(1, N):
        subordinate_num[A[i-1]-1] += 1
    return subordinate_num

if __name__ == '__main__':
    get_subordinate_num()