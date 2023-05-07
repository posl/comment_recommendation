def main():
    N = int(input())
    c = 0
    for i in range(1, N+1):
        if '7' not in str(i) and '7' not in oct(i)[2:]:
            c += 1
    print(c)
