def main():
    a, b, k = map(int, input().split())
    count = 0
    while True:
        if a >= b:
            break
        a *= k
        count += 1
    print(count)
