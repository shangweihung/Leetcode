class Solution(object):
    def evalRPN(self, tokens):

        operator=["+","-","*","/"]
        stack=[]
        for i in tokens:
            if i not in operator:
                stack.append(int(i))
            else:
                num1=stack.pop()
                num2=stack.pop()
                if i=="+":
                    stack.append(num2+num1)
                elif i=="-":
                    stack.append(num2-num1)
                elif i=="*":
                    stack.append(num2*num1)
                elif i=="/":
                    if num1*num2>=0:
                        stack.append(num2//num1)
                    else:
                        ans=num2//num1+1 if num2%num1!=0 else num2/num1
                        stack.append(ans)
            
        return stack[0]


if __name__=='__main__':
    print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])==22)
