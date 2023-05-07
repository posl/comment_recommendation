def main():
    N = int(input())
    for i in range(1, int(N**0.5)+1):
        if N%i == 0:
            print(i)
            if i != N//i:
                print(N//i)
