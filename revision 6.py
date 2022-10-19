def groupAnagrams(strs):
    anagrams={}
    for i in strs:
        sortedword="".join(sorted(i))
        if sortedword in anagrams:
            anagrams[sortedword].append(i)
        else:
            anagrams[sortedword]=(i)
    return list(anagrams.values())
strs=["Banana"]
print(groupAnagrams(strs))
