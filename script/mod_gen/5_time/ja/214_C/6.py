def get_input_data():
    n = int(input())
    s_list = list(map(int, input().split()))
    t_list = list(map(int, input().split()))
    return n, s_list, t_list

if __name__ == '__main__':
    get_input_data()