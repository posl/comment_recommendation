def main():
    n = int(input())
    a = input().split()
    for i in range(n):
        if int(a[i]) % 2 == 0:
            if int(a[i]) % 3 == 0 or int(a[i]) % 5 == 0:
                pass
            else:
                print("DENIED")
                exit()
    print("APPROVED")
