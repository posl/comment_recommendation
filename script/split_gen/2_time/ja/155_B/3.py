def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    for a in a_list:
        if a % 2 == 0:
            if a % 3 == 0 or a % 5 == 0:
                continue
            else:
                print("DENIED")
                exit()
    print("APPROVED")
