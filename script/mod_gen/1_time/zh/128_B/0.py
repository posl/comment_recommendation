def get_input():
    n = int(input())
    data = []
    for i in range(n):
        data.append(input().split(' '))
    return n, data

if __name__ == '__main__':
    get_input()