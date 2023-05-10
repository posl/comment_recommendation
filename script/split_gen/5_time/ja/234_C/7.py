def main():
    k = int(input())
    ans = 0
    for i in range(1, k + 1):
        ans = ans * 10 + 2
    print(ans)
