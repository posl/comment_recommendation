def main():
    x = int(input())
    y = 100
    count = 0
    while y < x:
        y = int(y * 1.01)
        count += 1
    print(count)
