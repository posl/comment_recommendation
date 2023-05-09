def main():
    a,b,c = map(int, input().split())
    print(max(9*10**2 + a+b+c, a*10**2 + b*10 + c + b*10 + c))
