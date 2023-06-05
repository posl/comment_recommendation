def main():
    input = raw_input()
    inputs = input.split()
    a = int(inputs[0])
    b = int(inputs[1])
    if a > 9 or b > 9:
        print -1
    else:
        print a * b
