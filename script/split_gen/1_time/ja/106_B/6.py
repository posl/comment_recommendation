def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1,2):
        if i % 2 == 1:
            if count(i) == 8:
                ans += 1
    print(ans)
