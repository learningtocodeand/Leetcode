class Solution(object):
    def isIsomorphic(self, s, t):
        d={}
        for i in range(0,len(s)):
            if s[i] not in d:
                if t[i] in d.values():
                    return False
                d[s[i]]=t[i]
            else:
                if not (d[s[i]]==t[i]):
                    return False
        return True
        