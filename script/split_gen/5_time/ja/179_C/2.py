def main():
    N = int(input())
    ans = 0
    for i in range(1,N):
        for j in range(1,N):
            for k in range(1,N):
                if i*j+k == N:
                    ans += 1
    print(ans)
