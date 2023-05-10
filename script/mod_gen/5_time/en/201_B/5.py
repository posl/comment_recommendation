def main():
    n = int(input())
    mountains = {}
    for i in range(n):
        s, t = input().split()
        mountains[s] = int(t)
    mountains = sorted(mountains.items(), key=lambda x:x[1], reverse=True)
    print(mountains[1][0])

if __name__ == '__main__':
    main()