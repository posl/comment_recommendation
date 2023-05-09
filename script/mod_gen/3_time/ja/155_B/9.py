def check():
    n = int(input())
    a_list = list(map(int, input().split()))
    for a in a_list:
        if a % 2 == 0 and (a % 3 != 0 and a % 5 != 0):
            return False
    return True
print("APPROVED" if check() else "DENIED")

if __name__ == '__main__':
    check()