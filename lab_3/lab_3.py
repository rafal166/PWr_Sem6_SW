import re

slownik = {};
naglowek = """From: author@example.com

User-Agent: Thunderbird 1.5.0.9 (X11/20061227)

MIME-Version: 1.0

To: editor@example.com"""

regex = r"(.*):(.*)"
result = re.findall(regex, naglowek)

for res in result :
	slownik[res[0].strip()] = res[1].strip()

print(slownik)