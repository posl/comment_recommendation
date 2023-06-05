def get_data():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = [int(input()) for _ in range(q)]
    return n, q, a, k

if __name__ == '__main__':
    get_data()