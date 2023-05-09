def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i*j <= N and (i*j)**(1/2) % 1 == 0:
                ans += 1
    print(ans)
