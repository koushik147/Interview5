class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        self.flag = True # assigning the flag value to true
        self.mid = self.findmid(head) # finding the mid value by calling findmid function
        midnext = self.mid.next # storing the mid next value 
        headB = self.reverse(midnext) # reversing themid next and storing in headB
        midnext = None
        self.compare(head,headB) # calling recurse function of head, headB
        return self.flag # returning flag
        
    def findmid(self,head):
        slow = head
        fast = head
        while fast.next!=None and fast.next.next!=None: # run until fast next and fast.next.next is not none
            slow = slow.next # incrementing slow by 1
            fast = fast.next.next # incrementing fast by 2
        return slow # returning slow
        
    def reverse(self,head):
        
        prev = None
        curr = head
        
        while curr: # run until curr is not none
            temp = curr.next # assiging curr next value to temp
            curr.next = prev # chaning the pointer and assigning to prev
            prev = curr # assigning curr to prev
            curr = temp # assinging temp to curr
        return prev
        
    def compare(self,head1,head2):
        
        pa = head1 # assigning head1 to pa pointer 
        pb = head2 # assinging head2 to pointer pb
        
        while pb != None:
            
            if not (pa.val==pb.val): # if pa and pb is not equal
                self.flag = False
                
            pa = pa.next # incrementing pa to next
            pb = pb.next # incrementing pb to next
            
        return self.flag # returning flag