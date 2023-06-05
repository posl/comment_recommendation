def get_input():
    N,T = [int(i) for i in input().split()]
    c_t = []
    for i in range(N):
        c_t.append([int(i) for i in input().split()])
    return N,T,c_t

if __name__ == '__main__':
    get_input()