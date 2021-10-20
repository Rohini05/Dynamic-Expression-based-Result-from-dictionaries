def search(arr, x):
    y = list(x.split(" "))
    print(y)
    z=[]
    for key, value in arr.items():
        if key in y:
            if len(y) == 1 or "or" in y :
                print(value)
                break;
            else:
                if "and" in y :
                    z.append(value)
                    string =''.join([str(elem) for elem in z])
                    print("hgh",string)

    return -1
  
arr = {'A':'Hello', 'B': 'World', 'C': 'Buddy'}
x=input("Enter the expression:")
search(arr, x)
# print(x, "is present at index",
#       search(arr, x))