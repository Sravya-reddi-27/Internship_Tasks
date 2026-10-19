# Problem: Weighted Uniform Strings
# HackerRank: https://www.hackerrank.com/challenges/weighted-uniform-string/problem

s = input().strip()
n = int(input())

weights = set()
previous = ""
current_weight = 0

for ch in s:
    weight = ord(ch) - ord('a') + 1

    if ch == previous:
        current_weight += weight
    else:
        current_weight = weight

    weights.add(current_weight)
    previous = ch

for _ in range(n):
    x = int(input())

    if x in weights:
        print("Yes")
    else:
        print("No")