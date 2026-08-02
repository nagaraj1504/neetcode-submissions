class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)

        for num in nums:
            res[num] += 1

        ans = sorted(
            res.items(),
            key=lambda item: item[1],
            reverse=True
        )[:k]

        return [item[0] for item in ans]