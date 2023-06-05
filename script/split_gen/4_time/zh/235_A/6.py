def main():
    abc = int(input())
    a = int(abc/100)
    b = int(abc/10)%10
    c = abc%10
    print(a+b+c+b+c+a+c+a+b+c)
