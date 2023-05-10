def main():
    # input
    n = input()
    # solve
    ans = n.replace('1', 'x').replace('9', '1').replace('x', '9')
    # output
    print(ans)

if __name__ == '__main__':
    main()