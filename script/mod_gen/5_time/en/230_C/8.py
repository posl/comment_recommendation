def paint(N, A, B, P, Q, R, S):
    result = ''
    for i in range(P, Q+1):
        for j in range(R, S+1):
            if (i+j)%2 == 0:
                result += '#'
            else:
                result += '.'
        result += '\n'
    return result

if __name__ == '__main__':
    paint()