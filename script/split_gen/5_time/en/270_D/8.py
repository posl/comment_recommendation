def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(a[-1]+1)
    b = [0] * (n+1)
    for i in range(1, n+1):
        for j in a:
            if i - j < 0:
                break
            b[i] = max(b[i], 1 - b[i-j])
    print('First' if b[n] == 1 else 'Second')
