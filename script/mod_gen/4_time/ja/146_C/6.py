def main():
    A,B,X = map(int, input().split())
    ans = 0
    for i in range(1,10):
        if A*i+B*len(str(i)) > X:
            break
        ans = i
    print(ans)

if __name__ == '__main__':
    main()