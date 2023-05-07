def main():
    a, b = map(int, input().split())
    c = 1
    for i in range(2, a+1):
        if a%i==0 and b%i==0:
            c += 1
    print(c)
