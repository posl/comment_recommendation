def get_str():
    n = int(input())
    str_list = []
    for i in range(n):
        str_list.append(input().split())
    return str_list

if __name__ == '__main__':
    get_str()