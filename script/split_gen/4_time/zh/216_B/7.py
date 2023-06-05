def main():
    n = int(input())
    name_list = []
    for i in range(n):
        name_list.append(input())
    if len(set(name_list)) == len(name_list):
        print("No")
    else:
        print("Yes")
