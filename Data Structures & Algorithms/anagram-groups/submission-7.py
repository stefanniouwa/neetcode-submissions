class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        bigList = {}
        for word in strs:
            zero_rows = [0] * 26
            for char in word:
                index = ord(char) - 97
                zero_rows[index] = zero_rows[index] + 1
            zero_rows = tuple(zero_rows)

            if zero_rows in bigList:
                anagram_list = bigList.get(zero_rows)
                anagram_list.append(word)
                bigList[zero_rows] = anagram_list
            else: 
                bigList[zero_rows] = [word]

        return list(bigList.values())