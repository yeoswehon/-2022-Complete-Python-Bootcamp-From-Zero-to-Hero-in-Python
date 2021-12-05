# randomtings

Random programs I did to explore some computing concepts.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Points to take note:

Tuples are similar to lists, the only key difference is that the elements in tuples are immutable.

.count('<element>')

.index('<element>')

There are only two tuple methods count() and index() that a tuple object can call.
  
Sets are unordered collections of unique elements, meaning there can only be one representative of the same object. If you attempt to add the same element to the set twice, it does not work.

.add(element stuff)  
  
Python list pop() is an inbuilt function in Python that removes and returns the last value from the List or the given index value.

.append() adds an element

Merging of lists is possible

The sort() method sorts the elements of a given list in a specific ascending or descending order. It arranges elements but does not return anything from the list. Hence, my_sorted_list = new_list.sort() is meaningless

.reverse() reverses the elements in the list
  
character: h e l l o

index: 0 1 2 3 4

reverse index: 0 -4 -3 -2 -1

\n new line \t tab

for i in enumerate("abcde"):

(0,a), (1,b), ...., etc kind of like tuple index matching
  
mylist1 = [1,2,3]
mylist2=['a','b','c']
 
for item in zip(mylist1,mylist2):
    print (item)
 
mylist=[letter for letter in mystring] where mystring = 'hello'
  
d = { 'k1':100, 'k2':200}

d['k3'] = 300

d.keys() k1 k2 k3

d.values() 100 200 300

d.items() tuples k1 paired 100, k2 paired 200, etc
  
type function reveals the data type
 
help function reveals the python documentation syntax
