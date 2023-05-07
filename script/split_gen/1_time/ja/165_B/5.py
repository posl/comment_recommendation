def main():
    x = int(input())
    y = 100
    count = 0
    while y < x:
        y = y + int(y * 0.01)
        count += 1
    print(count)
