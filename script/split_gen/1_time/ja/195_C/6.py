def main():
    N = int(input())
    ans = 0
    for i in range(3,len(str(N))+1):
        ans += (N-10**(i-1)+1) * (i-1)
    print(ans)
