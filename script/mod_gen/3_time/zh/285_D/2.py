def get_input():
    n = int(input())
    s_t = []
    for i in range(n):
        s_t.append(input().split())
    return n, s_t

if __name__ == '__main__':
    get_input()