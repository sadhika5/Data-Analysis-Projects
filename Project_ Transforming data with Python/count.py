import read
import collections
df=read.load_data()
combined_string=""
for index, row in df.iterrows():
    combined_string+=str(row["headline"])
    
combined_string=combined_string.lower()
words = combined_string.split(" ")
hundred_words=collections.Counter(words).most_common(100)
print(hundred_words)

