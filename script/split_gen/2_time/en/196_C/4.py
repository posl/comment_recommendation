def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        if len(str(i)) % 2 == 0 and str(i)[:int(len(str(i))/2)] == str(i)[int(len(str(i))/2):]:
            count += 1
    print(count)
