arr=[55,6,58,3,44,6,454,62,47,625,5,514,8]
searchterm=int(input("Enter the search term"))
notfound=True
for i in arr:
    if searchterm==i:
        print("Search element found")
        notfound=False

if notfound:
    print("Not Found")
