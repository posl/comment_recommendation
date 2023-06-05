def get_input():
    line1 = input().split()
    n = int(line1[0])
    k = int(line1[1])
    T = []
    for i in range(n):
        line = input().split()
        T.append([int(i) for i in line])
    return n, k, T

if __name__ == '__main__':
    get_input()