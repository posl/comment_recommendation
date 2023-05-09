def main():
    N = int(input())
    if N == 1:
        print(1)
        return
    counter = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            if str(i)[-1] == str(j)[0] and str(i)[0] == str(j)[-1]:
                counter += 1
    print(counter)
