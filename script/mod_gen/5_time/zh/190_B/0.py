def get_input():
    n, s, d = map(int, input().split())
    spells = []
    for i in range(n):
        spells.append(list(map(int, input().split())))
    return n, s, d, spells

if __name__ == '__main__':
    get_input()