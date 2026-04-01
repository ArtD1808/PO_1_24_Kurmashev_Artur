s = input()

s = s.lower()
s = s.replace(" ", "")

print(s == s[::-1])