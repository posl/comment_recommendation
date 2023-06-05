def max_monster(N,A,B):
    max_monster = 0
    for i in range(N):
        if B[i] >= A[i]:
            max_monster += A[i]
            B[i] = B[i] - A[i]
            A[i] = 0
        else:
            max_monster += B[i]
            A[i] = A[i] - B[i]
            B[i] = 0
        if B[i] >= A[i+1]:
            max_monster += A[i+1]
            B[i] = B[i] - A[i+1]
            A[i+1] = 0
        else:
            max_monster += B[i]
            A[i+1] = A[i+1] - B[i]
            B[i] = 0
    return max_monster

if __name__ == '__main__':
    max_monster()