def main():
    # input
    a, b = map(int, input().split())
    # compute
    if a <= 8 and b <= 8:
        ans = "Yay!"
    else:
        ans = ":("
    # output
    print(ans)
