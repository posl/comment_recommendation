def fizzbuzz(n):
    return n*(n+1)//2 - (n//3)*(n//3 + 1)//2*3 - (n//5)*(n//5 + 1)//2*5 + (n//15)*(n//15 + 1)//2*15
n = int(input())
print(fizzbuzz(n))

if __name__ == '__main__':
    fizzbuzz()