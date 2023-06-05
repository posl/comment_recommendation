def read_int_list():
    return list(map(int, input().split()))
N, C = read_int_list()
services = []
for _ in range(N):
    services.append(read_int_list())

if __name__ == '__main__':
    read_int_list()