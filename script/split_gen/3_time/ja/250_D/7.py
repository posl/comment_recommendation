def main():
    N = int(input())
    ans = 0
    for p in range(2, 1000000):
        for q in range(2, 1000000):
            k = p * q ** 3
            if k > N:
                break
            if is_prime(p) and is_prime(q):
                ans += 1
    print(ans)
