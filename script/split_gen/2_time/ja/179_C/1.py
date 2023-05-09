def main():
    n = int(input())
    count = 0
    for a in range(1, n+1):
        for b in range(1, n+1):
            c = n - a * b
            if c > 0:
                count += 1
    print(count)
