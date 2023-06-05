def main():
    n = int(input())
    x = 0
    for i in range(1, n + 1):
        x += i
        if x >= n:
            print(i)
            break
