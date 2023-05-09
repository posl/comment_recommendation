def main():
    n = int(input())
    i = 1
    ans = []
    while i * i <= n:
        if n % i == 0:
            ans.append(i)
            if i != n // i:
                ans.append(n // i)
        i += 1
    ans.sort()
    for i in ans:
        print(i)
