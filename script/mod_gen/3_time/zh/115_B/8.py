def get_input():
    N = int(raw_input())
    p = []
    for i in range(N):
        p.append(int(raw_input()))
    return N, p

if __name__ == '__main__':
    get_input()