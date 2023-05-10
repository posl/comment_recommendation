def rotate(string):
    reversed = string[::-1]
    rotated = ""
    for char in reversed:
        if char == "6":
            rotated += "9"
        elif char == "9":
            rotated += "6"
        else:
            rotated += char
    return rotated

if __name__ == '__main__':
    rotate()