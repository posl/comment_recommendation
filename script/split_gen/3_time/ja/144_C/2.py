def main():
    n = int(input())
    i = 1
    j = 1
    ans = 0
    while i * j < n:
        if i > j:
            j += 1
        else:
            i += 1
        ans += 1
    print(ans)
