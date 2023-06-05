def get_input():
    n_x = input().split()
    n = int(n_x[0])
    x = int(n_x[1])
    a = input().split()
    a = [int(i) for i in a]
    return n, x, a

if __name__ == '__main__':
    get_input()