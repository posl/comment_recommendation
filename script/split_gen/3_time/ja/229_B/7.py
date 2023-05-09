def main():
    A, B = map(int, input().split())
    ans = "Hard"
    if A + B < 10:
        ans = "Easy"
    print(ans)
