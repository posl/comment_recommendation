def main():
    n,k = map(int,input().split())
    count = 0
    for i in range(1,n+1):
        if i >= k:
            count += 1/n
        else:
            count += (1/n) * ((1/2)**(len(bin(k)[2:])-1))
    print(count)
