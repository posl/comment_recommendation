def main():
    X = int(input())
    ans = 0
    bal = 100
    while bal < X:
        ans += 1
        bal = int(bal * 1.01)
    print(ans)
