#find longest substring in string s that is in alphabetical order
s = 'azcbobobegghakl'
longest_substring = ""
if(len(s) == 1):
    longest_substring = s
else:
    for i in range(0, len(s)-1):
        substring = s[i]
        x = i
        while (x < len(s) - 1 and s[x] <= s[x+1]):
            substring += s[x+1]
            x += 1
        if(len(substring) > len(longest_substring)):
            longest_substring = substring
print("Longest substring in alphabetical order is:", longest_substring)