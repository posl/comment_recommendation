def main():
    abc = input()
    abc = int(abc)
    a = abc // 100
    b = (abc // 10) % 10
    c = abc % 10
    print((a+b+c)*(a*100+b*10+c))
