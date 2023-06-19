def get_input():
    in_str = input()
    in_list = in_str.split()
    n = int(in_list[0])
    c = int(in_list[1])
    service_list = []
    for i in range(n):
        service_str = input()
        service_list.append(service_str.split())
    return n, c, service_list

if __name__ == '__main__':
    get_input()