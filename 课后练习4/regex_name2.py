import re

s = '{"name": "Alyssa \\"P.\\" Hacker", "college": "MIT"}'

pattern = r'"name":\s*"((?:\\.|[^"\\])*)"'
print(re.search(pattern, s).group(1))
