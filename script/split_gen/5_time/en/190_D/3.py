def main():
    n = int(input())
    ans = 0
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            if i%2 == 1:
                ans += 2
            if i*i == n:
                ans -= 1
    print(ans)
