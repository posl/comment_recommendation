def main():
    n = int(input())
    ans = 0
    for i in range(1, 10**6):
        if (2*n-i*i+i)%(2*i) == 0:
            ans += 1
    print(ans*2)
