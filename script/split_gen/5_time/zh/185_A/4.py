def main():
    a = input()
    a_list = a.split()
    a_list = [int(x) for x in a_list]
    a_list.sort()
    print(a_list[0])
