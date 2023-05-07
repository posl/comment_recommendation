def get_input():
    n = int(input())
    shops = []
    for _ in range(n):
        a, p, x = map(int, input().split())
        shops.append((a, p, x))
    return shops

if __name__ == '__main__':
    get_input()