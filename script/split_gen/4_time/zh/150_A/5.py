def main():
    input_str = input()
    input_list = input_str.split()
    k = int(input_list[0])
    x = int(input_list[1])
    if k * 500 >= x:
        print("Yes")
    else:
        print("No")
