def read_ints():
    return list(map(int, input().split()))
n, s = read_ints()
cards = []
for i in range(n):
    a, b = read_ints()
    cards.append((a, b))

if __name__ == '__main__':
    read_ints()