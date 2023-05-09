def main():
    n = int(input())
    t = list(map(int, input().split()))
    print(sum(t)-max(t)+max(t)//2)
main()

if __name__ == '__main__':
    main()