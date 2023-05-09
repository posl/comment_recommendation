def main():
    N = int(input())
    ans = []
    i = 1
    while i**2 <= N:
        if N % i == 0:
            ans.append(i)
            if i**2 != N:
                ans.append(N//i)
        i += 1
    ans.sort()
    for a in ans:
        print(a)
