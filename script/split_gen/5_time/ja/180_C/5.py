def main():
    N = int(input())
    ans = set()
    i = 1
    while i * i <= N:
        if N % i == 0:
            ans.add(i)
            ans.add(N // i)
        i += 1
    for a in sorted(ans):
        print(a)
