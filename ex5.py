str = raw_input("Δώσε μου ημερομηνία σε μορφή dd/mm/yyyy")
strlist = ["SATURDAY", "SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"]
list = str.split("/")
vmonth = int(list[1])
vday= int(list[0])
vfyear = int(list[2])
if (vmonth < 3):
    vmonth = vmonth + 12
    vfyear = vfyear - 1

vcentury = vfyear/100
vyear = vfyear%100
dweek = (( vday + ((( vmonth + 1)* 26)/10)+vyear+(vyear/4)+(vcentury/4))+(5*vcentury))%7
print strlist[dweek]

