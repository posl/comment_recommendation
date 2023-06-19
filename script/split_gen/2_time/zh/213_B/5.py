def main():
    n = int(input())
    scores = [int(i) for i in input().split()]
    min_value = min(scores)
    scores = [i for i in scores if i != min_value]
    print(scores.index(min(scores))+1)
