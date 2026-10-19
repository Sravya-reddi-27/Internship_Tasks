# Problem: CamelCase
# HackerRank: https://www.hackerrank.com/challenges/camelcase/problem

s = input().strip()

if s:
    count = 1

    for ch in s:
        if ch.isupper():
            count += 1

    print(count)
else:
    print(0)