def main():
    input = raw_input()
    input = input.split()
    input = map(int, input)
    input.sort()
    print input[2]*10 + input[1] + input[0]
