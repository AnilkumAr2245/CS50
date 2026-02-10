months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    date=input("Date: ").strip()
    if "/" in date:
        try:
            m,d,y=date.split("/")
            m=int(m)
            d=int(d)
            y=int(y)
            if 1<=m<=12 and 1<=d<=31:
                print(f"{y:04d}-{m:02d}-{d:02d}")
                break
        except ValueError:
            pass
    else:
        try:
            m,d,y=date.split(" ")
            if not d.endswith(","):
                raise ValueError
            d=d.replace(",","")
            y=int(y)
            if m in months:
                m=months.index(m)+1
                d=int(d)
                if 1<=d<=31:
                    print(f"{y:04d}-{m:02d}-{d:02d}")
                    break
        except ValueError:
            pass


