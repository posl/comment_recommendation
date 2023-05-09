def main():
    y = int(input())
    while True:
        y += 1
        if y % 4 == 2:
            break
    print(y)
