filename  = input("enter file name")
s = filename.split('.')
if len(s)>1:
    extension=s[-1]
    print("the extension of theb file is",extension)
else:
    print("file has no extension")
