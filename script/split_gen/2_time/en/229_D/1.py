def main():
    S = input()
    K = int(input())
    count = 0
    for i in range(len(S)):
        if S[i] == 'X':
            count += 1
        else:
            if K > 0:
                K -= 1
                count += 1
            else:
                break
    print(count)
