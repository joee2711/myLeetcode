from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_ = max(candies)
        res_ = []
        for i in candies:
            if i+extraCandies >= max_:
                res_.append(True)
            else:
                res_.append(False)

        return res_
    

if __name__ == '__main__':
    obj = Solution()
    print(obj.kidsWithCandies([4,2,1,1,2],1))