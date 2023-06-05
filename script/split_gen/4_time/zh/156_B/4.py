def main():
    n,k = map(int,input().split())
    # print(n,k)
    # print(type(n),type(k))
    count = 0
    while n > 0:
        n = n//k
        count += 1
    print(count)
