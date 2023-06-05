def main():
    input_str = input()
    sum = 0
    for i in range(4):
        if input_str[i] == "+":
            sum += 1
        else:
            sum -= 1
    print(sum)
