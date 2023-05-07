def main():
    # input
    S = input()
    # compute
    if S == 'SUN':
        ans = 7
    elif S == 'MON':
        ans = 6
    elif S == 'TUE':
        ans = 5
    elif S == 'WED':
        ans = 4
    elif S == 'THU':
        ans = 3
    elif S == 'FRI':
        ans = 2
    elif S == 'SAT':
        ans = 1
    # output
    print(ans)

if __name__ == '__main__':
    main()