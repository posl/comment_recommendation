def convert_to_base_10(x, base):
    result = 0
    for i in range(len(x)):
        result += int(x[-(i+1)]) * (base ** i)
    return result
x = input()
m = int(input())

if __name__ == '__main__':
    convert_to_base_10()