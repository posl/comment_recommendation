def f(N, Q, A, X):
    result = []
    for i in range(Q):
        count = 0
        while(True):
            if A[0] == X[i]:
                break
            if A[0] > X[i]:
                A[0] -= 1
            else:
                A[0] += 1
            count += 1
            A.sort()
        result.append(count)
    return result

if __name__ == '__main__':
    f()