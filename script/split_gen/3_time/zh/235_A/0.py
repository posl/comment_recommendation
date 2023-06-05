def main(abc):
    abc = int(abc)
    a = abc // 100
    b = abc // 10 % 10
    c = abc % 10
    print(a * 100 + b * 10 + c + b * 100 + c * 10 + a + c * 100 + a * 10 + b)
