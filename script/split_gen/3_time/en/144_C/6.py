def main():
    N = int(input())
    for i in range(1, 10**6):
        if i*(i+1) >= 2*N:
            print(i + (N - i*(i-1)//2 - 1)//i)
            break
