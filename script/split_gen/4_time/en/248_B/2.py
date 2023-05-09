def main():
    a, b, k = map(int, input().split())
    if a >= b:
        print(0)
    else:
        count = 0
        while a < b:
            a *= k
            count += 1
        print(count)
