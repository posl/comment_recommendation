def pascal(N):
    if N == 1:
        return [1]
    elif N == 2:
        return [1,1]
    else:
        p = pascal(N-1)
        return [1] + [p[i-1] + p[i] for i in range(1,N-1)] + [1]

if __name__ == '__main__':
    pascal()