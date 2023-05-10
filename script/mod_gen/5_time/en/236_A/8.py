def swap_string():
    string = input("Enter the String: ")
    a, b = map(int, input("Enter the values of a and b: ").split())
    a = a - 1
    b = b - 1
    string = list(string)
    string[a], string[b] = string[b], string[a]
    string = ''.join(string)
    print(string)
swap_string()

if __name__ == '__main__':
    swap_string()