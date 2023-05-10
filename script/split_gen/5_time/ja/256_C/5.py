def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    count = 0
    for i in range(1, 101):
        for j in range(1, 101):
            for k in range(1, 101):
                if i + j == h1 and j + k == h2 and i + k == h3 and i + j + k == w1 and i + j + k == w2 and i + j + k == w3:
                    count += 1
    print(count)
