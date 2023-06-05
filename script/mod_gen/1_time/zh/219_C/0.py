def get_input():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    return x, n, s

if __name__ == '__main__':
    get_input()