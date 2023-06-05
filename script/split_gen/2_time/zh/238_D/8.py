def main():
    N = int(input())
    mod = 998244353
    answer = 0
    for i in range(1, 10):
        tmp = 1
        for j in range(1, N + 1):
            tmp = (tmp * i) % mod
            answer = (answer + tmp) % mod
    print(answer)
    return
