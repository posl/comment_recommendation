def main():
    # input
    C1, C2, C3 = input().split()
    # compute
    if C1 == C2 and C2 == C3:
        result = 'Won'
    else:
        result = 'Lost'
    # output
    print(result)

if __name__ == '__main__':
    main()