class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal=[]
        if(numRows==1):
            pascal=[[1]]
            
        elif numRows==2:
            pascal=[[1],[1,1]]
            
        else:
            pascal=[[1],[1,1]]
            for i in range (2,numRows):
                temprow=[1]
                for j in range (0,i-1):
                    temprow.append(pascal[i-1][j]+pascal[i-1][j+1])
                temprow.append(1)
                pascal.append(temprow)
        return pascal