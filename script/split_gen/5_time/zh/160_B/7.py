def main():
    x = int(input())
    y = x // 500
    z = (x - y * 500) // 5
    print(y * 1000 + z * 5)
