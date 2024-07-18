import re

# zero or more b's
s = re.compile('ab*')
print(s.findall("abbababbbaababababab"))

# one or more b's
s = re.compile("ab+")
print(s.findall("abbababbbaababababab"))

# two to three b's
string = "My name is bbar."
patter = 'b{2,3}'
match = re.search(patter, string)
if match:
    print("Match found!")
else:
    print("Match not found.")

# find sequence of lowercase letters joined by underscore
text = "aaa_Bb"
patter = '^[a-z]+_[a-z]+$'
if re.search(patter, text):
    print("Pattern found")
else:
    print("Not found")

# one upper letter followed by lower case
text = "zeEl"
patter = '[A-Z]+[a-z]+$'
if re.search(patter, text):
    print("Pattern found")
else:
    print("Not found")

# 'a' followed by anything ending in 'b'
text = "azeelbb"
pattern = '^a.*b$'
if re.search(pattern, text):
    print("Found")
else:
    print("Not found")

# matches a word at the beginning of a string.
string = " my name is zeel savaliya"
pattern = re.compile(r'^\w+')
if re.search(pattern, string):
    print(string)
else:
    print("String not found")

# matches a word at the end of a string, with optional punctuation.
string = "zeel savaliya!.."
pattern = re.compile(r'\w+\S*$')
if re.search(pattern, string):
    print("found")
else:
    print("Not found")

# matches a word containing 'z'
string = "aeel savaliya!.."
pattern = re.compile(r'\w*z.\w*')
if re.search(pattern, string):
    print("found")
else:
    print("Not found")

# matches a word containing 'z', not the start or end of the word.
string1 = "eezl savaliya"
pattern = re.compile(r'\Bz\B')
if re.search(pattern, string1):
    print("Found")
else:
    print("Not found")

# check that a string contains only a certain set of characters (in this case a-z, A-Z 0-9)
text = "zeel savaliya"
pattern = re.compile(r'^[a-zA-z0-9_]*$')
if re.search(pattern, text):
    print("Found")
else:
    print("Not found")

# starts each string with a specific number.
string = "zeel 11savaliya"
match = re.compile(r"^11")
if re.search(match, string):
    print("Yes")
else:
    print("No")

# remove leading zeros from an IP address.
ip = "216.08.094.1096"
string = re.sub(r'\.0*', '.', ip)
print(string)

# check for a number at the end of a string
text = "zeel savaliya11"
pattern = re.compile(r"11$")
if re.search(pattern, text):
    print("Found")
else:
    print("Not Found")

# search for literal strings within a string.
text = "The quick brown fox jumps over the lazy dog."
pattern = ['fox', 'dog', 'horse']
for patterns in pattern:
    print('Searching for "%s" in "%s" ->' % (pattern, text), )
    if re.search(patterns, text):
        print("pattern found")
    else:
        print("Pattern not found")

# search for a literal string in a string and also find the location within the original string where the pattern occurs.
text = "The quick brown fox jumps over the lazy dog."
word = 'fox'
match = re.search(word, text)
s = match.start()
e = match.end()
print('Found "%s" in "%s" from %d to %d ' % (match.re.pattern, match.string, s, e))

# find the substrings within a string.
text = 'Python exercises, PHP exercises, C# exercises'
match = 'exercises'
for i in re.findall(match, text):
    print('Found "%s"' % i)

# replace whitespaces with an underscore and vice versa.
text = 'Zeel Savaliya_11'
text = text.replace(" ", "_")
print(text)
text = text.replace("_", " ")
print(text)

# extract year, month and date from an URL.
url = "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
url1 = re.findall(r'/(\d{4})/(\d{1,2})/(\d{1,2})/', url)
print(url1)

# convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
dt1 = "2005-03-11"
dt = re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt1)
print(dt)
print(dt1)


#find regex for 0716.01, 2000, 198, 4080.06, 795/42, 794 0006
string = "0716.01, 2000, 198, 4080.06, 795/42, 794 0006"
match = re.findall(r'(^\d+\.\d+), (\d{4}), (\d{3}), (\d+\.\d+), (\d+/\d+), (\d+\s\d+)', string)
print(match)
        df['Date'] = df['Date'].astype(str)
        df['Ref'] = df['Ref'].astype(str)

        df.insert(4, 'accountNo', 0)
        df.insert(5,'narration', 0)
        df.insert(3, 'code', 0)

        df = df.dropna(axis='columns', how='all')

        regex = r'^\d{3}/*\d{3}$'
        df['accountNo'] = df['Date'].str.findall(regex)

        pattern = r'^\d+'
        for index, row in df.iterrows():
            if re.search(pattern, row['Ref']):
                df.at[index, 'code'] = row['Ref']
            else:
                df.at[index, 'narration'] = row['Ref']

        columns = ['Date', 'Type', 'Units', 'Debits', 'Credits', 'Balance', 'accountNo', 'narration', 'code']
        df = df[columns]
