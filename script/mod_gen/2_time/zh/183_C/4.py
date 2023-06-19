def get_data():
    n, k = map(int, input().split())
    time = []
    for i in range(n):
        time.append(list(map(int, input().split())))
    return n, k, time

if __name__ == '__main__':
    get_data()