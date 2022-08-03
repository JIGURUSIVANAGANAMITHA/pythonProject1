import re

txt = "Use of python in Machine Learning"
x = re.search("^Use.*Learnings$", txt)
if (x):
    print("Yes! We have a match!")
else:
    print("no match!")
