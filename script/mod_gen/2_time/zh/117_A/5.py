def get_input():
    n, k = map(int, input().split())
    sushi = []
    for i in range(n):
        sushi.append(list(map(int, input().split())))
    return n, k, sushi

if __name__ == '__main__':
    get_input()