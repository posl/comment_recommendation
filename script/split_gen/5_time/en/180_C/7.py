def main():
    n = int(input())
    l = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            l.append(i)
            if i != n // i:
                l.append(n // i)
    l.sort()
    print(*l, sep='\n')
