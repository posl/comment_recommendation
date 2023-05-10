def main():
    # input
    S = input()
    # compute
    if S == 'Monday':
        ans = 5
    elif S == 'Tuesday':
        ans = 4
    elif S == 'Wednesday':
        ans = 3
    elif S == 'Thursday':
        ans = 2
    elif S == 'Friday':
        ans = 1
    else:
        ans = 6
    # output
    print(ans)
