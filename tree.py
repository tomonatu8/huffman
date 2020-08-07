import numpy as np

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class binarytree:
    def __init__(self, num_list):
        self.root=None
        for node in num_list:
            self.insert(node)
    def insert(self,data):
        r=self.root
        if r==None:
            self.root=Node(data)
            return
        else:
            while True:
                rdata=r.data
                if rdata > data:
                    if r.left==None:
                        r.left=Node(data)
                        return
                    r=r.left
                elif rdata < data:
                    if r.right==None:
                        r.right=Node(data)
                        return
                    r=r.right
                else:
                    r.data=data
                    return
    def search(self,search):
        r=self.root
        if r==None:
            return None
        else:
            search_list=[]
            search_list.append(r)
            while len(search_list)>0:
                check=search_list.pop()
                if check.data==search:
                    return True
                if check.left is not None:
                    search_list.append(check.left)
                if check.right is not None:
                    search_list.append(check.right)
            return False
