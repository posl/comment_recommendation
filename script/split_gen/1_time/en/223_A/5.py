def main():
    # input
    X = int(input())
    # compute
    if X%100 == 0 and X != 0:
        ans = "Yes"
    else:
        ans = "No"
    # output
    print(ans)
