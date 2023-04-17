Synthesizing 10/10 solutions (Duplicates hidden)

=======

def main():
    N,K = map(int,input().split())
    if N%K == 0:
        print(0)
    else:
        print(1)

=======

def main():
  n,k = map(int,input().split())
  if n%k == 0:
    print(0)
  else:
    print(1)

=======

def main():
    N, K = map(int, input().split())
    print(N % K)

=======

def main():
    N, K = map(int, input().split())
    print(1 if N % K != 0 else 0)

=======

def main():
    #入力
    N, K = map(int, input().split())
    #出力
    print(N % K)
