def read_data():
    n = int(input())
    a_list = []
    b_list = []
    for i in range(n):
        a, b = map(int, input().split())
        a_list.append(a)
        b_list.append(b)
    return n, a_list, b_list

if __name__ == '__main__':
    read_data()