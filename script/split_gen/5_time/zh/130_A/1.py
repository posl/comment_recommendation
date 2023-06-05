def main():
    input_data = input()
    X = int(input_data.split()[0])
    A = int(input_data.split()[1])
    if X < A:
        print(0)
    else:
        print(10)
