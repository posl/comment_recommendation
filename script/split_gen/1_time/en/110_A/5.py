def main():
    a,b,c = [int(x) for x in input().split()]
    print(max(a+b+c, a+b*c, a*b+c, a*b*c, (a+b)*c, a*(b+c)))
