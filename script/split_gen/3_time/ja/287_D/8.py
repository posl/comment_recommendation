def main():
    # S = input()
    # T = input()
    S = 'beginner'
    T = 'contest'
    for i in range(len(T)+1):
        print('Yes' if T == S[i:i+len(T)] else 'No')
