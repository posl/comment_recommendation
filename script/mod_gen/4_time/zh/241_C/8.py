def get_input():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    return n, s

if __name__ == '__main__':
    get_input()