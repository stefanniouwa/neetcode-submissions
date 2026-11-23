class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        bigList = {}
        for i in range(len(strs)):
            wordA = strs[i]
            sorted_wordA = "".join(sorted(wordA))
            if sorted_wordA in bigList:
                anagram_list = bigList.get(sorted_wordA)
                anagram_list.append(wordA)
                bigList[sorted_wordA] = anagram_list
            else: 
                bigList[sorted_wordA] = [wordA]

        return list(bigList.values())