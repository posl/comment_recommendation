def get_list():
    n = int(input())
    v_list = list(map(int,input().split()))
    c_list = list(map(int,input().split()))
    return n,v_list,c_list

if __name__ == '__main__':
    get_list()