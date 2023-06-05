def main():
    abc = input()
    abc = int(abc)
    a = abc // 100
    b = (abc - a * 100) // 10
    c = abc - a * 100 - b * 10
    print(a * 100 + b * 10 + c + b * 100 + c * 10 + a + c * 100 + a * 10 + b)
