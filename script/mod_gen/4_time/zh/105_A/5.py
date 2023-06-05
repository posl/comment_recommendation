def get_input():
    line = raw_input()
    line = line.split(' ')
    n = int(line[0])
    k = int(line[1])
    return n, k

if __name__ == '__main__':
    get_input()