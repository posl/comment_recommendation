def main():
    # input
    n = int(input())
    # compute
    if -2**31 <= n < 2**31:
        ans = 'Yes'
    else:
        ans = 'No'
    # output
    print(ans)
