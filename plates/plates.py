def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not (2<=len(s)<=6):
        return False
    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    for i in s:
        if not (i.isalpha() or i.isdigit()):
            return False
    num_started=False
    for i in s:
        if i.isdigit():
            if not (num_started):
                if i=='0':
                    return False
                num_started=True
        else:
            if num_started:
                return False
    return True
main()
