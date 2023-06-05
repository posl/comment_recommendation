def get_input():
    n = int(input())
    x = []
    u = []
    for i in range(n):
        x.append(input())
        u.append(input())
    return n, x, u

if __name__ == '__main__':
    get_input()