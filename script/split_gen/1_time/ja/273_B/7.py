def main():
    x, k = map(int, input().split())
    #print(x, k)
    k = 10 ** k
    #print(k)
    x = x // k * k
    #print(x)
    x = x + k
    #print(x)
    x = x // k * k
    #print(x)
    print(x)
