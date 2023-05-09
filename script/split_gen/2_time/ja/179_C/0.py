def main():
    n = int(input())
    count = 0
    for a in range(1, n):
        for b in range(1, n):
            c = n - a * b
            if c > 0:
                count += 1
            else:
                break
    print(count)
