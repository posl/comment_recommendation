def get_input():
    n = int(input())
    if n < 1 or n > 100000:
        raise Exception('N is out of range')
    data = []
    for i in range(n):
        line = input().strip().split(' ')
        if len(line) != 2:
            raise Exception('Input format error')
        data.append((line[0], int(line[1])))
    return data

if __name__ == '__main__':
    get_input()