def main():
    N = int(input())
    S = [input() for i in range(N)]
    count = 0
    for s in S:
        if s == "For":
            count += 1
    if count > N / 2:
        print("Yes")
    else:
        print("No")
