def get_input():
    n, k = map(int, input().split())
    l_r = []
    for i in range(k):
        l_r.append(list(map(int, input().split())))
    return n, k, l_r

if __name__ == '__main__':
    get_input()