def main():
    y = int(input())
    while True:
        if y % 4 == 2:
            print(y)
            break
        else:
            y = y + 1
