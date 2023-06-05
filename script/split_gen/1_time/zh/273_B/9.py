def main():
    x,k = map(int, input().split())
    #print(x,k)
    for i in range(k):
        if x % (10**(i+1)) < 5 * 10**i:
            print(x - x % (10**(i+1)))
            break
        else:
            print(x + (10**(i+1) - x % (10**(i+1))))
            break
