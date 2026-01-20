class Solution(object):
    def romanToInt(self, s):
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        # d1=[]
        
        # for i in range(len(s)-1,-1,-1):
        #     d1.append(d[s[i]])
        # num=d1[0]
        # for j in range(1,len(d1)):
        #     if(d1[j-1]>d1[j]):
        #         num=num-d1[j]
        #     else:
        #         num=num+d1[j]
        # return num
        n=len(s)
        prev=d[s[n-1]]
        ans = d[s[n-1]]
        for i in range(n-2,-1,-1):
            if d[s[i]]<prev:
                ans = ans - d[s[i]]
            else:
                ans = ans + d[s[i]]
            prev=d[s[i]]
        return ans