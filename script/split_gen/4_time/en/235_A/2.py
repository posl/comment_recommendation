def main():
    num = input()
    num = int(num)
    a = num // 100
    b = (num % 100) // 10
    c = num % 10
    print(a + b + c)
