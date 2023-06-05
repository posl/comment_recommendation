def get_input():
    n = int(input())
    p_list = []
    for i in range(n):
        p_list.append(int(input()))
    return n, p_list

if __name__ == '__main__':
    get_input()