def main():
    n = int(input())
    s = input()
    result = ""
    for i in range(n):
        if s[i] == ",":
            if i % 2 == 0:
                result += ","
            else:
                result += "."
        else:
            result += s[i]
    print(result)
