def main():
    n = input()
    answer = ""
    for i in n:
        if i == "1":
            answer += "9"
        else:
            answer += "1"
    print(answer)
