def get_input():
    n = input()
    s = []
    for i in range(n):
        s.append(raw_input())
    return n, s

if __name__ == '__main__':
    get_input()