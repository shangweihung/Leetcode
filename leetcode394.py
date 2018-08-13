class Solution(object):
    def decodeString(self, s):
        num,char=[],[]
        i=0
        length=len(s)
        while i <length:
            index=i+1
            if s[i].isdigit():
                number=int(s[i])
                while index<length:
                    if s[index].isdigit():
                        number=number*10+int(s[index])
                        index+=1
                    else: 
                        break
                num.append(number)
            elif s[i]=='[' or s[i].isalpha():
                char.append(s[i])
            else:
                t=char.pop()
                tem=[]
                while t!='[':
                    tem.append(t)
                    t=char.pop()
                tem_char=num.pop()*''.join(tem[::-1])
                char.append(tem_char)
            
            i=index
        return ''.join(char)

if __name__=="__main__":
    assert Solution().decodeString("3[a]2[bc]")=="aaabcbc"
    assert Solution().decodeString("3[a2[c]]")=="accaccacc"
