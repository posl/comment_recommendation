def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        for j in range(i,N+1):
            for k in range(j,N+1):
                if i * j * k <= N:
                    ans += 1
    print(ans)
