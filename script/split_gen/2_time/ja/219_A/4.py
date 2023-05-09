def main():
    # input
    x = int(input())
    # compute
    if x < 40:
        ans = 40 - x
    elif x < 70:
        ans = 70 - x
    elif x < 90:
        ans = 90 - x
    else:
        ans = 'expert'
    # output
    print(ans)
