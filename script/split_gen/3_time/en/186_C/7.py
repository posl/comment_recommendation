def main():
    n = int(input())
    a = 0
    for i in range(1, n+1):
        if '7' not in str(i) and '7' not in oct(i)[2:]:
            a += 1
    print(a)
