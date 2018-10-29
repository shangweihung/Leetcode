class Solution(object):
    def meetroom(self,nums):
        starts,ends=[],[]

        for i in nums:
            starts.append(i[0])
            ends.append(i[1])

        starts.sort()
        ends.sort()

        s,e=0,0                

        rooms=0
        curr_room=0
        while s<len(starts):
            if starts[s]<ends[e]:
                curr_room+=1
                rooms=max(rooms,curr_room)
                s+=1
            else:
                curr_room-=1
                e+=1
        return rooms

class Solution2(object):
    def meetroom(self,nums):
        time=[]
        for i in nums:
            time.append((i[0],'start'))
            time.append((i[1],'end'))
        time.sort()

        cur_room=0;
        max_room=0;
        for t in time:
            if t[1]=='start':
                cur_room+=1
            elif t[1]=='end':
                cur_room-=1
            max_room=max(max_room,cur_room)

        return max_room
                        

if __name__ == "__main__":
    print( Solution2().meetroom([[0, 30],[15, 20],[5, 10]]) == 2)
    print( Solution2().meetroom([[7, 10],[2, 4]])==1)
