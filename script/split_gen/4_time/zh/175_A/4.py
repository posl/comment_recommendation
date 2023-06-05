def main():
    S = input()
    count = 0
    max = 0
    for i in range(3):
        if S[i] == "R":
            count = count + 1
            if count > max:
                max = count
        else:
            count = 0
    print(max)
