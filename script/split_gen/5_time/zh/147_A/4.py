def main():
    a = input()
    a_list = a.split()
    a_list = [int(i) for i in a_list]
    if sum(a_list) >= 22:
        print("bust")
    else:
        print("win")
