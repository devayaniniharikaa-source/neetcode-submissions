class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        close2open={")":"(","}":"{", "]":"["}
        for i in s:
            if( i in close2open):
                if(stack and stack[-1]==close2open[i]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
        