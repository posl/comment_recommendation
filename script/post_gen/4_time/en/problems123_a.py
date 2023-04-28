Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())
    if (e - a) > k:
        print(":(")
    else:
        print("Yay!")

=======
Suggestion 2

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())
    if e - a > k:
        print(':(')
    else:
        print('Yay!')

=======
Suggestion 3

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())
    if e - a > k:
        print(":(")
    else:
        print("Yay!")

=======
Suggestion 4

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())
    if e - a <= k:
        print("Yay!")
    else:
        print(":(")

=======
Suggestion 5

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())
    if (e - a) <= k:
        print("Yay!")
    else:
        print(":(")

main()

Haskell

{-# LANGUAGE OverloadedStrings #-} import qualified Data.ByteString.Char8 as BS import Data.Maybe (fromJust) main :: IO () main = do [a,b,c,d,e,k] <- map (fst . fromJust . BS.readInt) . BS.words <$> BS.getLine print $ if k >= e - a then "Yay!" else ":("

Java

import java.io.BufferedReader; import java.io.InputStreamReader; import java.io.IOException; public class Main { public static void main(String[] args) throws IOException { BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); int a = Integer.parseInt(br.readLine()); int b = Integer.parseInt(br.readLine()); int c = Integer.parseInt(br.readLine()); int d = Integer.parseInt(br.readLine()); int e = Integer.parseInt(br.readLine()); int k = Integer.parseInt(br.readLine()); if (e - a <= k) { System.out.println("Yay!"); } else { System.out.println(":("); } } }

Python

a = int(input()) b = int(input()) c = int(input()) d = int(input()) e = int(input()) k = int(input()) print(':(' if e-a>k else 'Yay!')

Ruby

a, b, c, d, e, k = 6.times.map { gets.to_i } puts e - a > k ? ':(' : 'Yay!'

Scala

object Main extends App { val a, b, c, d, e, k = scala.io.StdIn.readInt() println(if (e - a > k) ":(" else "Yay!") }

TypeScript

import * as fs from "fs"; const [a, b, c, d, e, k]: number[] = fs.readFileSync("/dev/stdin", "utf8").trim().split("

").map(Number); if (e - a <= k) { console.log("Yay!"); } else { console.log(":("); }

5 - 2 = 3

5 - 4 = 1

5 - 3 = 2

5 - 1 = 4

5 - 5 = 0

5 - 0 = 5

=======
Suggestion 6

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())

    if (e - a) <= k:
        print("Yay!")
    else:
        print(":(")
