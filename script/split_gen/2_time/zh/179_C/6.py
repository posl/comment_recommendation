def main():
    n = int(input())
    count = 0
    for c in range(1, n):
        for a in range(1, n):
            if n >= a * c:
                b = n - a * c
                if b <= a:
                    count += 1
                else:
                    break
            else:
                break
    print(count)
