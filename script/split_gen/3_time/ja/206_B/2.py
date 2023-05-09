def main():
    N = int(input())
    ans = 0
    for i in range(1, 10**5):
        ans += i
        if ans >= N:
            print(i)
            break
