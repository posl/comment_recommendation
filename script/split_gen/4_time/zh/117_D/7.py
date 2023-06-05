def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if n == 1:
        print(k ^ a[0])
        return
    max_xor = 0
    a.sort()
    for i in range(n - 1):
        for j in range(i + 1, n):
            xor = a[i] ^ a[j]
            if xor > k:
                break
            else:
                if xor > max_xor:
                    max_xor = xor
    print(max_xor)
