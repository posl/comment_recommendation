def main():
    n = int(input())
    a = 1
    b = 1
    count = 0
    while a * b < n:
        if a < b:
            a += 1
        else:
            b += 1
        count += 1
    print(count)
