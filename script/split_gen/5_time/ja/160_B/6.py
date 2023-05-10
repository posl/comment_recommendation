def main():
    x = int(input())
    count = 0
    count += x // 500 * 1000
    x = x % 500
    count += x // 5 * 5
    print(count)
