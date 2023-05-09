def main():
    Y = int(input())
    for i in range(Y, 3000):
        if i % 4 == 2:
            print(i)
            break
