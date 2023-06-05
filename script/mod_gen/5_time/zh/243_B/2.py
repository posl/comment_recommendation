def get_same_num(A, B):
    same_num = 0
    for i in range(len(A)):
        if A[i] == B[i]:
            same_num += 1
    return same_num

if __name__ == '__main__':
    get_same_num()