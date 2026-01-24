string=input("Input:")
ns=""
for s in string:
    if s in ["a","e","i","o","u","A","E","I","O","U"]:
        ns+=""
    else:
        ns+=s
print(ns)
