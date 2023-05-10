def main():
    N = int(input())
    ans = set()
    for i in range(2, int(N**0.5)+1):
        x = i*i
        while x <= N:
            ans.add(x)
            x *= i
    print(N-len(ans))
