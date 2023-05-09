def main():
    a, b, x = map(int, input().split())
    #print("a,b,x:", a, b, x)
    #print("x / a:", x / a)
    #print("x / b:", x / b)
    if x / a > 10**9:
        print(10**9)
    elif x / b > 10**9:
        print(10**9)
    else:
        print(0)
