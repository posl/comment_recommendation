def main():
    S = input()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    for i in range(5):
        if S == days[i]:
            print(5 - i)
            break
