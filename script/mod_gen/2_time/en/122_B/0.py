def main():
    s = input()
    s = s.replace('A', '1')
    s = s.replace('C', '2')
    s = s.replace('G', '3')
    s = s.replace('T', '4')
    l = s.split('5')
    ans = 0
    for i in l:
        ans = max(ans, len(i))
    print(ans)

if __name__ == '__main__':
    main()