def main():
    p = int(input())
    k = 0
    for i in range(10,0,-1):
        k += p//math.factorial(i)
        p %= math.factorial(i)
    print(k)
