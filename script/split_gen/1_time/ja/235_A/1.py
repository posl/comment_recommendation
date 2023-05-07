def main():
    abc = int(input())
    a = abc // 100
    b = (abc - a * 100) // 10
    c = (abc - a * 100 - b * 10)
    print(abc + b * 100 + c * 10 + c * 100)
