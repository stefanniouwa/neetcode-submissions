class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        bigList = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in bigList:
                anagram_list = bigList.get(sorted_word)
                anagram_list.append(word)
                bigList[sorted_word] = anagram_list
            else: 
                bigList[sorted_word] = [word]

        return list(bigList.values())