def is_split(pins):
    if pins[0] == "0":
        return "No"
    else:
        for i in range(1, 10):
            if pins[i] == "1":
                if pins[i-1] == "1" and pins[i+1] == "1":
                    return "Yes"
                else:
                    return "No"
pins = input()
print(is_split(pins))

if __name__ == '__main__':
    is_split()