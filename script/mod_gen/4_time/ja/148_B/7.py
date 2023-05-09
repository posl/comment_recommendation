def main():
    n = int(input())
    s, t = input().split()
    answer = ''
    for i in range(n):
        answer += s[i] + t[i]
    print(answer)

if __name__ == '__main__':
    main()