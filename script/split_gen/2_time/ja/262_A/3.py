def main():
    Y = int(input())
    while True:
        if Y % 4 == 2:
            print(Y)
            break
        else:
            Y += 1
