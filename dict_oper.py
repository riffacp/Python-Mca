thisdict = {"name":"rifa","roll_num":18,"reg_num":"25mca","dept":"MCA"}
thisdict["total_mark"]=98
print(thisdict)
total = thisdict["total_mark"]

if total >90:
    grade="A grade"
elif total >80:
    grade="B grade"
elif total >70:
    grade="C grade"
elif total >60:
    grade="D grade"
elif total <60:
    grade="Failed"

thisdict["Grade"]=grade
del thisdict["roll_num"]
print(thisdict)
