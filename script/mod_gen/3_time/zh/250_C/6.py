def main():
    n, q = map(int, input().split())
    balls = [i+1 for i in range(n)]
    for i in range(q):
        x = int(input())
        if balls[x-1] == n:
            balls[x-1], balls[x-2] = balls[x-2], balls[x-1]
        else:
            balls[x-1], balls[x] = balls[x], balls[x-1]
    print(' '.join(map(str, balls)))

if __name__ == '__main__':
    main()