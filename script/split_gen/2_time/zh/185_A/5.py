def main():
    a,b,c = map(int, input().split())
    print((a*b*c-1)/(a*b+b*c+c*a-a-b-c))
