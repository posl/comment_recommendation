def main():
    k = int(input())
    ans = ""
    for i in range(k):
        ans += chr(i+ord("A"))
    print(ans)
