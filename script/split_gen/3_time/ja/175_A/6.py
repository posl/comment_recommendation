def main():
    S = input()
    ans = 0
    count = 0
    for i in S:
        if i == "R":
            count += 1
        else:
            if count > ans:
                ans = count
            count = 0
    if count > ans:
        ans = count
    print(ans)
