def main():
    n = int(input())
    score = {}
    for i in range(n):
        s, t = input().split()
        t = int(t)
        if s not in score:
            score[s] = t
    print(n - len(score) + 1)

if __name__ == '__main__':
    main()