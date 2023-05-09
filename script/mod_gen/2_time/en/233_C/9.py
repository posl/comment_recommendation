def get_primes(n): #n以下の素数を返す
    if n == 2:
        return [2]
    elif n < 2:
        return []
    s = [i+1 for i in range(1, n, 2)]
    m = int(n ** 0.5)
    half = (n+1)//2 - 1
    i = 0
    m2 = 3
    while m2 <= m:
        if s[i]:
            j = (m2*m2-3)//2
            s[j] = 0
            while j < half:
                s[j] = 0
                j += m2
        i = i + 1
        m2 = 2*i + 3
    return [2] + [el for el in s if el]

if __name__ == '__main__':
    get_primes()