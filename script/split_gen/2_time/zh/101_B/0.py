def main():
    N = int(input())
    sum = 0
    for i in range(len(str(N))):
        sum += int(str(N)[i])
    if N % sum == 0:
        print("Yes")
    else:
        print("No")
