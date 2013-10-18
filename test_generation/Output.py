'''
---------------------------------------------------
Author			:	Tuyen Nguyen
Name			:	Output.py
Date Create		:	15/10/2013
Last Comit		:	19/10/2013
'''

import re
import math
import unittest
import itertools
import input 


var=[]                                #luu cac bien duoi dang list of array number
ret=[]                                #luu cac string tra ve [ return " Not null" -> Not null ] vao list

vflag=False
rflag=False
check=0


'''
-------------------------------------------------
Kiem tra cac khoang co bi trung nhau khong cua 1 bien
-----------------------------------------------
'''
#START checkdup
def checkdup(a):
    i=0
    while 1:
        for j in range(len(a)-1):
            if(a[i]<a[j]<a[i+1]):
                return False
        i=i+2
        if(i==len(a)):
            break
    return True
#END checkdup

'''
-------------------------------------------------
Kiem tra cac khoang trong moi bien co bi trung nhau khong
-----------------------------------------------
'''
#START checkvar
def checkvar(a):
    check=0
    for arrchild in a:
        if(checkdup(arrchild)):
            check+=1
        else:
            return False
    if(check==len(a)):
        return True
#END checkvar

'''
-------------------------------------------------------------
Doc file input.py
Doc mang cac bien  va cac gia tri tra ve
--------------------------------------------------------------
'''
#START read
with open('input.py','r') as f:
    for line in f:
        if 'main' in line:
            rflag=True
        if (rflag==True) & ('return' in line):
            ret.append(line.strip().lstrip("return '").rstrip("'"))
        if line.strip().startswith("'''"):
            vflag=True
            check=check+1
            if(check==1):
                continue
            else:
                vflag=False
        if vflag:
            var.append(map(int,re.findall(r'[0-9]+',line.strip())))
#END read

'''
---------------------------------------------------------------
Tim cac khoang tuong duong cua mot bien
'''

#START findAvg
def findAvg(lst):
    tmplst=[]
    i=0
    while 1:
        if(i>len(lst)-1):
            break
        tmplst.append( int(round((lst[i]+lst[i+1])/2)) )
        i=i+2
    print tmplst
    return tmplst
#END findAvg
'''
--------------------------------------------------------------
Tim tat ca cac khoang tuong duong cua cac bien
EX:
a=[[1,4,6,8,10,16],[4,6]]
>>>
lst=[[2, 7, 13], [5]]
'''
#START findAll
def findAll(lst):
    tmpst=[]
    
    for child in lst:
        tmpst.append(findAvg(child))
        continue
    return tmpst
#END findAll
#Unittest
try:
            
    class output(unittest.TestCase):
        pass

    def test_generator(*args):
        def test(self):
            self.assertEqual(input.main(*args),1)
        return test

    if __name__=="__main__":
        if checkvar(var)==False:
            raise Exception("wrong input")
        else :
            for arr in itertools.product(*findAll(var)):
                test_name='test_'+str(arr)
                test=test_generator(*arr)
                setattr(output,test_name,test)
        unittest.main()
except Exception as e:
    print "wrong input"
