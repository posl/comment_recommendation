def main():
    N = int(input())
    S = input()
    if 'na' in S:
        print(S.replace('na','nya'))
    else:
        print(S)

if __name__ == '__main__':
    main()