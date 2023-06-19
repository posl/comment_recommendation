def main():
    # input
    n = int(input())
    a = list(map(int, input().split()))
    # compute
    for i in a:
        if i%2 == 0:
            if i%3 != 0 and i%5 != 0:
                print("DENIED")
                exit()
    # output
    print("APPROVED")
