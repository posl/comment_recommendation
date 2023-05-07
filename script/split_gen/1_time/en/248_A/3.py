def main():
    # input
    s = input()
    # compute
    s = set(s)
    for i in range(10):
        if str(i) not in s:
            ans = i
            break
    # output
    print(ans)
