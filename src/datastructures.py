
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self.next_id = 1
        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return  randint(1, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        if isinstance(member, list):
            for m in member:
                m["id"]=self._generateId()
                self._members.append(m)
        else:        
            member["id"]=self._generateId()
            self._members.append(member)
        pass

    def delete_member(self, id):
        # fill this method and update the return
        for (index,member) in enumerate(self._members):
            if(member["id"]==id):
                self._members.pop(index)
        pass

    def get_member(self, id):
         for (index,member) in enumerate(self._members):
            if(member["id"]==id):  
             return self._members[index]

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members

    def edit_member(self,id,newmember):
        for (index,member) in enumerate(self._members):
            if(member["id"]==id): 
                self._members[index]=newmember
