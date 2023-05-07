def main():
    N = int(input())
    T = input()
    count = 0
    for i in T:
        if i == "S":
            count += 1
    if count > N/2:
        print(N)
    else:
        print(N - 2*count)
