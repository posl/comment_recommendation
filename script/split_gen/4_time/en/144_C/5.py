def main():
    n = int(input())
    m = int(n**0.5)
    if m*m == n:
        print(m*2-2)
    elif m*(m+1) >= n:
        print(m*2-1)
    else:
        print(m*2)
