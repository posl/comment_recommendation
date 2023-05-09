def main():
    x = int(input())
    if x == 0:
        print(0)
    else:
        print(1000 * (x // 500) + 5 * ((x % 500) // 5))
