class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        bigList = {}
        for word in strs:
            counts = [0] * 26
            for char in word:
                index = ord(char) - ord("a")
                counts[index] += 1
            counts = tuple(counts)

            if counts in bigList:
                
                bigList[counts].append(word)
            else: 
                bigList[counts] = [word]

        return list(bigList.values())