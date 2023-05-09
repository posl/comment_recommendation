def main():
    k = int(input())
    ans = 0
    for i in range(1,k+1):
        if i%2 == 0:
            ans += (k-i)//2 + 1
    print(ans)
