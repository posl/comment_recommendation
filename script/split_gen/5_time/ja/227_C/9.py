def main():
    N = int(input())
    ans = 0
    for i in range(1, int(N**(1/3))+1):
        for j in range(i, int(N**(1/2))+1):
            if i*j > N:
                break
            ans += 1
    print(ans)
