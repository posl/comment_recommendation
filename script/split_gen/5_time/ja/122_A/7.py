def main():
    # input
    b = input()
    # compute
    if b == 'A':
        ans = 'T'
    elif b == 'T':
        ans = 'A'
    elif b == 'C':
        ans = 'G'
    elif b == 'G':
        ans = 'C'
    # output
    print(ans)
