def main():
    n = int(input())
    ans = 0
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            ans = max(ans, i)
            while n % i == 0:
                n //= i
    if n != 1:
        ans = max(ans, n)
    print(ans-1 if ans else 0)
