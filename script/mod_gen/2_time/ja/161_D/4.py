def runrun(n):
    if n > 10**9:
        return
    yield n
    a = n % 10
    for b in [a-1, a, a+1]:
        if 0 <= b <= 9:
            yield from runrun(10*n+b)
K = int(input())
print(sorted(runrun(n)) [K-1])

if __name__ == '__main__':
    runrun()