def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    max_a = max(a)
    for i in range(n):
        if a[i] == max_a:
            max_a2 = max(a[:i] + a[i + 1:])
    for i in range(n):
        if a[i] == max_a:
            print(max_a2)
        else:
            print(max_a)
main()
I got 90 points. This is my first submission.
I go

if __name__ == '__main__':
    main()