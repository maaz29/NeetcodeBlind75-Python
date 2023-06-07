class Solution:
    def isAnagram(self, test: str, word: str) -> bool:
        if len(test) != len(word):
            return False
        my_dict = collections.defaultdict(int)
        for char in test:
            my_dict[char]+=1
        for char in word:
            my_dict[char]-=1
        return all(x==0 for x in my_dict.values())
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        obj = Solution()
        temp = []
        for word in strs:
            temp.append(word)
            strs.remove(word)
            for check in strs:
                if obj.isAnagram(word, check):
                    temp.append(check)
                    strs.remove(check)
            output.append(temp)
        return output