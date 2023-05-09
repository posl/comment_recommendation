def max_allowance(a,b,c):
    print(max(a+b+c, a*b*c, (a+b)*c, a*(b+c)))

if __name__ == '__main__':
    max_allowance()