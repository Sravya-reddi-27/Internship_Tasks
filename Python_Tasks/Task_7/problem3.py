# Problem: Mars Exploration
# HackerRank: https://www.hackerrank.com/challenges/mars-exploration/problem

s = input().strip()
expected = "SOS" * (len(s) // 3)

count = 0
for a, b in zip(s, expected):
    if a != b:
        count += 1

print(count)