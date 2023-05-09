def is_ok(mid):
    sum = 0
    for i in range(N-1):
        sum += A[i]
    sum += mid
    if sum / N >= M:
        return True
    else:
        return False

if __name__ == '__main__':
    is_ok()