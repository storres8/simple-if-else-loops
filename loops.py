if 2>3:
    print("two is greater than three")
else:
    print("lies")
# prints out lies

a = 3
b = 90
c = 23.9
if a > b and  b < c:
    print("this makes sense")
elif a>b or b>c:
    print("now this makes sense")
else:
    print("I have no idea man")
# prints out "now this makes sense" since you only need one true value
# to persist for the entire value to be true with an or statement
