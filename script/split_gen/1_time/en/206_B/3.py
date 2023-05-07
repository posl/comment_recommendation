def main():
    n = int(input())
    i = 1
    total = 0
    while total < n:
        total += i
        i += 1
    print(i - 1)
