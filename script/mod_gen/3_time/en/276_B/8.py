def get_numbers():
    N,M = map(int, input().split())
    numbers = []
    for i in range(M):
        numbers.append(list(map(int, input().split())))
    return N, M, numbers

if __name__ == '__main__':
    get_numbers()