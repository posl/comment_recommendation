def problems107_b():
    h, w = map(int, input().split())
    matrix = []
    for i in range(h):
        matrix.append(input())
    matrix = list(filter(lambda x: '#' in x, matrix))
    matrix = list(zip(*matrix))
    matrix = list(filter(lambda x: '#' in x, matrix))
    matrix = list(zip(*matrix))
    for i in matrix:
        print(''.join(i))

if __name__ == '__main__':
    problems107_b()