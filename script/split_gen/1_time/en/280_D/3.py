def main():
    K = int(input())
    prime = []
    i = 2
    while i*i <= K:
        if K % i == 0:
            prime.append(i)
            while K % i == 0:
                K //= i
        i += 1
    if K > 1:
        prime.append(K)
    ans = 1
    for p in prime:
        i = p
        while i <= K:
            i *= p
        ans *= i//p
    print(ans)
main()
