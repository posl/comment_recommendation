def main():
    a, b, c, d, e = [int(input()) for _ in range(5)]
    print(((a + 9) // 10 + (b + 9) // 10 + (c + 9) // 10 + (d + 9) // 10 + (e + 9) // 10) * 10 - 9)
