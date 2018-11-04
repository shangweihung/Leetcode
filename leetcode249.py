import collections

class Solutions(object):
    def groupStrings(self,strings):
        group=collections.defaultdict(list)
        for s in strings:
            group[self.hashStr(s)].append(s)

        result=[]
        for i in group.keys():
            result.append(group[i])
        return result


    def hashStr(self,s):
        base=ord(s[0])
        hashcode=''

        for i in range(len(s)):
            if ord(s[i])-base>=0:
                hashcode+=str(ord(s[i])-base)
            else:
                hashcode+=str(ord(s[i])-base+26)
        return hashcode

if __name__=="__main__":
    print(Solutions().groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))
