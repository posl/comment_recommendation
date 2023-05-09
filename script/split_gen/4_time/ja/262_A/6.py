def main():
    y = int(input())
    while y <= 3000:
        y += 1
        if y % 4 == 2:
            print(y)
            break
    return
