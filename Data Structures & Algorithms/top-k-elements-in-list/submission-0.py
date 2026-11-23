class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bigList = {}
        for num in nums:
            if num in bigList.keys():
                bigList[num] += 1
            else:
                bigList[num] = 1

        sorted_dict = dict(sorted(bigList.items(), key=lambda item: item[1], reverse=True))

        topK_list = list(sorted_dict.keys())

        return topK_list[:k]
