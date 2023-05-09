def get_input():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    return n, arr

if __name__ == '__main__':
    get_input()