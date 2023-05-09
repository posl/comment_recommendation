def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        if i*(i+1)/2 > N:
            break
        if (N-i*(i+1)/2)%i == 0:
            count += 1
    print(count*2)
