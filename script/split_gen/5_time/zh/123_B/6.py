def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    print(min(a%10 and 10-a%10 or 0, b%10 and 10-b%10 or 0, c%10 and 10-c%10 or 0, d%10 and 10-d%10 or 0, e%10 and 10-e%10 or 0) + a + b + c + d + e)
