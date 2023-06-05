def main():
    a, b = map(int, input().split())
    a1 = a // 100
    a2 = a % 100 // 10
    a3 = a % 10
    b1 = b // 100
    b2 = b % 100 // 10
    b3 = b % 10
    print(max(a1+a2+a3, b1+b2+b3))
