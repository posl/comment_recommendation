def main():
    # code goes here
    n = int(input())
    ans = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            m = n // i - i
            if m % 2 == 1:
                continue
            m //= 2
            if m > 0:
                ans += 1
    print(ans * 2)
