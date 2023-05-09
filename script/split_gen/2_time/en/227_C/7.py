def main():
    N = int(input())
    ans = 0
    for i in range(1,int(N**0.5)+1):
        for j in range(1,int(N**0.5)+1):
            for k in range(1,int(N**0.5)+1):
                if i*j*k <= N:
                    ans += 1
    print(ans)
