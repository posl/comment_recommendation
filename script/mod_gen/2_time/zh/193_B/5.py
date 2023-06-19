def get_input():
    n = int(input())
    a_list = []
    p_list = []
    x_list = []
    for i in range(n):
        a, p, x = map(int, input().split())
        a_list.append(a)
        p_list.append(p)
        x_list.append(x)
    return n, a_list, p_list, x_list

if __name__ == '__main__':
    get_input()