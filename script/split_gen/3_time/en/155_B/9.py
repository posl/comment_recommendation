def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in a:
        if i % 2 == 1:
            continue
        if i % 3 != 0 and i % 5 != 0:
            print("DENIED")
            return
    print("APPROVED")
    return
