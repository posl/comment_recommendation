def main():
    X = int(input())
    for i in range(-1000, 1001):
        for j in range(-1000, 1001):
            if i ** 5 - j ** 5 == X:
                print(i, j)
                exit(0)
