def main():
    x = int(input())
    y500 = x // 500
    y5 = x % 500 // 5
    print(y500 * 1000 + y5 * 5)
