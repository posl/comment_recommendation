def get_input_data():
    n, s, d = map(int, input().split())
    xy = [list(map(int, input().split())) for _ in range(n)]
    return n, s, d, xy

if __name__ == '__main__':
    get_input_data()