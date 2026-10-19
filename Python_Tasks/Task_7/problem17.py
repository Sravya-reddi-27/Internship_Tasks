# Problem: Separate the Numbers
# HackerRank: https://www.hackerrank.com/challenges/separate-the-numbers/problem

q = int(input())

for _ in range(q):
    s = input().strip()
    found = False

    for length in range(1, len(s) // 2 + 1):
        first = int(s[:length])
        current = first
        parts = ""

        while len(parts) < len(s):
            parts += str(current)
            current += 1

        if parts == s:
            print("YES", first)
            found = True
            break

    if not found:
        print("NO")