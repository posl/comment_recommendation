def get_list():
    N = int(input())
    p_list = input().split()
    p_list = [int(i) for i in p_list]
    return N,p_list

if __name__ == '__main__':
    get_list()