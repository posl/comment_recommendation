def main():
    n = int(input())
    a = list(map(int, input().split()))
    flag = True
    for i in a:
        if i % 2 == 0 and (i % 3 != 0 and i % 5 != 0):
            flag = False
            break
    if flag:
        print("APPROVED")
    else:
        print("DENIED")
