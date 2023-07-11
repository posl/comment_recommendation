def read_data():
    n = int(input())
    data = []
    for i in range(n):
        data.append(input())
    return n, data

if __name__ == '__main__':
    read_data()