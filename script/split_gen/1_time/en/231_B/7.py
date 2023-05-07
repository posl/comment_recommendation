def main():
    num = int(input())
    input_list = []
    for i in range(num):
        input_list.append(input())
    print(max(set(input_list), key=input_list.count))
