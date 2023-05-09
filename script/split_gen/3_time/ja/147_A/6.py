def main():
    a_list = list(map(int, input().split()))
    if sum(a_list) >= 22:
        print("bust")
    else:
        print("win")
