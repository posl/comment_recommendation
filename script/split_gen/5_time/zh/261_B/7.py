def main():
    n = int(input())
    result = [input() for i in range(n)]
    for i in range(n):
        for j in range(n):
            if result[i][j] == 'W':
                if result[j][i] != 'L':
                    print('不正确')
                    return
            elif result[i][j] == 'L':
                if result[j][i] != 'W':
                    print('不正确')
                    return
            elif result[i][j] == 'D':
                if result[j][i] != 'D':
                    print('不正确')
                    return
    print('正确')
    return
