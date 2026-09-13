import re

s = '{"name": "Alyssa P. Hacker", "college": "MIT"}'

# 贪婪版本
greedy = r'"name":\s*"(.*)"'
print("greedy:", re.search(greedy, s).group(1))

# 非贪婪版本
nongreedy = r'"name":\s*"(.*?)"'
print("nongreedy:", re.search(nongreedy, s).group(1))
