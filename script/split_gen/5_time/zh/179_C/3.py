def main():
    N = int(input())
    count = 0
    for i in range(1,int(N**0.5)+1):
        if N%i == 0:
            if N//i != i:
                count += (N//i-1)
            else:
                count += (N//i-1)
    print(count)
