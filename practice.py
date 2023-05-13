# output = hElLo gOoD mOrNiNg
s="hello good morning"
x=s.split()
for word in x:
    st=" "
    for j in range(len(word)):
        if j%2==0:
            st+=word[j].lower()
        else:
            st+=word[j].upper()
    print(st, end=" ")
