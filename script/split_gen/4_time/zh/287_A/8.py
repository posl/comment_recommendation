def main():
    n = int(input())
    votes = []
    for i in range(n):
        votes.append(input())
    if votes.count("For") > n//2:
        print("Yes")
    else:
        print("No")
