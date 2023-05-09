def main():
    input_line = input().split()
    n = int(input_line[0])
    x = int(input_line[1])
    y = int(input_line[2])
    if n == 1:
        print(0)
    else:
        print((n-1)*x+y)
