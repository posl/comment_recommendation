def main():
    l = int(input())
    l -= 12
    ans = 1
    for i in range(1, 11):
        ans *= l + i
        ans //= i
    print(ans)
