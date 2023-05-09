def main():
    N = int(input())
    ans = 0
    for i in range(1,16):
        ans += (N//(10**i)-N//(10**(i+1)))*i
    print(ans)
