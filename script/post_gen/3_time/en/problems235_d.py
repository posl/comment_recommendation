Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, n = map(int, input().split())
    ans = 0
    while n > 1:
        if n % a == 0:
            n //= a
            ans += 1
        elif n % 10 == 1:
            n //= 10
            ans += 1
        else:
            ans = -1
            break
    print(ans)

=======
Suggestion 2

def main():
    a, n = map(int, input().split())
    ans = 0
    while n > 1:
        if n % a == 0:
            n //= a
            ans += 1
        elif n % 10 == 0:
            n //= 10
            ans += 1
        else:
            n -= 1
            ans += 1
    print(ans)

main()

=======
Suggestion 3

def main():
    a, n = map(int, input().split())
    ans = 0
    while n > 1:
        if n % a == 0:
            n //= a
            ans += 1
        elif n % 10 == 1:
            n = (n - 1) // 10
            ans += 1
        else:
            ans = -1
            break
    print(ans)

=======
Suggestion 4

def main():
    a, n = map(int, input().split())
    ans = 0
    while n > 1:
        if n % a == 0:
            n //= a
        elif n % 10 == 1:
            n //= 10
        else:
            print(-1)
            return
        ans += 1
    print(ans)

=======
Suggestion 5

def main():
    a, n = map(int, input().split())
    count = 0
    while n > 1:
        if n % a == 0:
            n //= a
        else:
            if n % 10 == 0:
                n //= 10
            else:
                print(-1)
                exit()
        count += 1
    print(count)

=======
Suggestion 6

def main():
    a, n = map(int, input().split())
    if n == 1:
        print(0)
        return
    if a == 2:
        print(n.bit_length())
        return
    count = 0
    while n > 1:
        if n % a == 0:
            n //= a
        elif n % 10 == 1:
            n //= 10
        else:
            print(-1)
            return
        count += 1
    print(count)

=======
Suggestion 7

def main():
    a, n = map(int, input().split())
    if n == 1:
        print(-1)
        return
    if a == 2:
        print(n)
        return
    if a == n:
        print(n + 1)
        return
    if a > n:
        print(2)
        return
    visited = [False] * 10 ** 6
    visited[1] = True
    q = [(1, 1)]
    while q:
        x, cnt = q.pop(0)
        if x == n:
            print(cnt)
            return
        nx = (x * a) % 10 ** 6
        if not visited[nx]:
            visited[nx] = True
            q.append((nx, cnt + 1))
        if x % 10 != 0:
            nx = (x % 10) * 10 ** (len(str(x)) - 1) + x // 10
            if not visited[nx]:
                visited[nx] = True
                q.append((nx, cnt + 1))
    print(-1)

=======
Suggestion 8

def main():
    a, n = map(int, input().split())
    if n % a == 0:
        print(-1)
        return
    x = 1
    i = 0
    while x != n:
        x = x * a
        if x % 10 == 0:
            x = x // 10
        else:
            x = x % 10
        i += 1
    print(i)

=======
Suggestion 9

def main():
    a, n = map(int, input().split())
    if n == 1:
        print(0)
        return
    if a == 2:
        print(len(bin(n)[2:]))
        return
    if a == 10:
        print(len(str(n)))
        return
    if n % a == 1:
        print(1)
        return
    ans = 1
    x = 1
    while True:
        x = x * a % n
        ans += 1
        if x == 1:
            print(ans)
            return
        if ans > n:
            print(-1)
            return

main()

The code is written in Python3.

=======
Suggestion 10

def main():
    a, n = map(int, input().split())
    #a = 2
    #n = 767090
    count = 0
    while n > 1:
        if n % a != 0:
            if n % 10 == 0:
                break
            else:
                n = int(str(n)[-1] + str(n)[:-1])
                count += 1
        else:
            n = n // a
            count += 1
    if n == 1:
        print(count)
    else:
        print(-1)
