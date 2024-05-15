import re
pattern = r'P[a-z]'
text = "Python is a great programming language"
matches = re.findall(pattern, text)
print("Matches:", matches)