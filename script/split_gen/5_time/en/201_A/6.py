def main():
    # input
    a1, a2, a3 = map(int, input().split())
    # solve
    if a3 - a2 == a2 - a1:
        ans = "Yes"
    else:
        ans = "No"
    # output
    print(ans)
