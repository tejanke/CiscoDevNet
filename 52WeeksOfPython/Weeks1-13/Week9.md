Review
* Quokka review
  * nmap scan
* comparisons
* if a == b
* if a not in b
* if a != b
* lower()
* copying, assignment, deep copy
  * assignment
    * a = b
    * a points to b, like a symbolic link
  * copy
    * from copy import copy
    * a = copy(b)
    * a shallow copy that only copies the first level, no nested lists or dictionaries
    * most used in data science when you have millions of objects
  * deep copy
    * from copy import deepcopy
    * a = deepcopy(b)
    * a complete copy of the original
    * most used when you need a real copy
* classes