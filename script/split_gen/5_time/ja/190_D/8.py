def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if (i*(i+1))//2 == N:
            ans += 1
        elif (i*(i+1))//2 > N:
            break
    print(ans*2)
