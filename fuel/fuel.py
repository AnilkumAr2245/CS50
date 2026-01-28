def main():
    fuel=get_value()
    print(fuel)
def get_value():
    while True:
        try:
            f=input("Fraction: ")
            x,y=f.split("/")
            x=int(x)
            y=int(y)
            if x<0 or y<=0 or x>y:
                continue
            fuel = (x / y) * 100
        except(ValueError,ZeroDivisionError):
            continue
        else:
            if (99<=fuel):
                return("F")
            elif(1>=fuel):
                return("E")
            else:
                v=round(fuel)
                return(f"{v}%")


main()



