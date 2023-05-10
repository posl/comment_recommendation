def main():
    A,B = map(int, input().split())
    ans = B/A
    ans = round(ans,4)
    print('{:.3f}'.format(ans))
    return

if __name__ == '__main__':
    main()