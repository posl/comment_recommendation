def main():
    num = int(input())
    count = 0
    for i in range(1, num + 1):
        if i < 1000:
            continue
        elif i < 1000000:
            count += 1
        elif i < 1000000000:
            count += 2
        elif i < 1000000000000:
            count += 3
        elif i < 1000000000000000:
            count += 4
        elif i < 1000000000000000000:
            count += 5
        elif i < 1000000000000000000000:
            count += 6
        elif i < 1000000000000000000000000:
            count += 7
        elif i < 1000000000000000000000000000:
            count += 8
        elif i < 1000000000000000000000000000000:
            count += 9
