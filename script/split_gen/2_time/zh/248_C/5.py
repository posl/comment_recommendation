def main():
    a,b,k = map(int,input().split())
    count = 0
    while a<b:
        a += a*(k-1)
        count += 1
    print(count)
