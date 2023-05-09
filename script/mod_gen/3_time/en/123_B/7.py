def main():
    # input
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    # compute
    ans = 0
    if A%10 != 0:
        A = ((A//10)+1)*10
    if B%10 != 0:
        B = ((B//10)+1)*10
    if C%10 != 0:
        C = ((C//10)+1)*10
    if D%10 != 0:
        D = ((D//10)+1)*10
    if E%10 != 0:
        E = ((E//10)+1)*10
    ans = A + B + C + D + E
    # output
    print(ans)

if __name__ == '__main__':
    main()