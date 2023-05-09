def main():
    num = int(input())
    input_list = input().split(" ")
    output_list = [0] * num
    for i in range(num):
        output_list[int(input_list[i]) - 1] = i + 1
    print(*output_list)
