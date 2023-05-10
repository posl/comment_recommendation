def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    ans = "No"
    if sum(A) - (len(A) // 2) <= X:
        ans = "Yes"
    print(ans)
