def main():
    k = int(input())
    n = 0
    while k > 0:
        n += 1
        if '2' in str(n):
            k -= 1
    print(n)
