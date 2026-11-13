import random

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c=='*':
                stack and stack.pop()
            else:
                stack.append(c)

        return ''.join(stack)



if __name__ == '__main__':
    obj = Solution()
    print(obj.removeStars('erase*****'))



asdasd