def main():
    S = input()
    count = 0
    for i in range(len(S)):
        if S[i] == "v":
            count += 1
    print(count * (count - 1) // 2)
