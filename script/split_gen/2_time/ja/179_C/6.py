def main():
    N = int(input())
    ans = 0
    for i in range(1, N):
        if i*i > N:
            break
        for j in range(1, N):
            if i*j > N:
                break
            if i*j < N:
                ans += 1
    print(ans)
