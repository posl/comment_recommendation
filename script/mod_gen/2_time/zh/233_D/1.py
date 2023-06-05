def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if n//i != i:
                divisors.append(n//i)
    return divisors
N, X = map(int, input().split())
balls = []
for i in range(N):
    balls.append(list(map(int, input().split()))[1:])
divisors = get_divisors(X)
ans = 0
for d in divisors:
    for i in range(N):
        if d in balls[i]:
            ans += 1
            break
print(ans)

if __name__ == '__main__':
    get_divisors()