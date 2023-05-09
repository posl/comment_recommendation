def main():
    n = input()
    ans = ''
    for i in range(len(n)):
        if n[i] == '1':
            ans += '9'
        elif n[i] == '9':
            ans += '1'
    print(ans)

if __name__ == '__main__':
    main()