def main():
    a,b,c = map(int,input().split())
    result = a+b+c
    result = max(result,(a+b)*c)
    result = max(result,a*(b+c))
    result = max(result,a*b*c)
    print(result)
