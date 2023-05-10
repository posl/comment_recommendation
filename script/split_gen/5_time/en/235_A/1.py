def main():
    abc = int(input())
    a = int(abc / 100)
    b = int(abc / 10) % 10
    c = int(abc % 10)
    print(a + b + c)
