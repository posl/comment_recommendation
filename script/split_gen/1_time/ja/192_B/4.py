def main():
    S = input()
    even = []
    odd = []
    for i in range(len(S)):
        if i % 2 == 0:
            even.append(S[i])
        else:
            odd.append(S[i])
    if all([s.islower() for s in odd]) and all([s.isupper() for s in even]):
        print('Yes')
    else:
        print('No')
