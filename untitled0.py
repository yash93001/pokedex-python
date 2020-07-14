import pandas as pd
import matplotlib.pyplot as plt
import os
import glob
import natsort 
#reading all the images
dir1 = r"C:\Users\yash1\Desktop\pokedex\pokemon_images"  

path1 = os.path.join(dir1,'*g')

files = glob.glob(path1)
files1= natsort.natsorted(files,reverse=False)

imag = []
for x in files1:
    img = plt.imread(x)
    imag.append(img)
    
#reading the dataset
data = pd.read_csv('pokemon.csv')

#main file

print("Pokedex\n")
print("Welcome Pokemon Lovers\n")
print("Search for a pokemon\n")
df1 =input("<A>Search by pokemon name\n<B>Search by pokemon ID\n(select A or B)\n")
df1 = df1.upper()
if(df1=="A"):
    print("Enter the name of the pokemon")
    name = input()
    name = name.lower().strip()
    dt = data[:].where(data['pokemon']==name)
    idx = dt.index[dt['pokemon']==name]
    st = dt[dt['id'].notnull()]    
    for i in st.columns:
        print(i," : ",st[i][idx[0]])
    plt.imshow(imag[idx[0]])
    plt.axis("off")   # turns off axes
    plt.axis("tight")  # gets rid of white border
    plt.axis("image")  # square up the image instead of filling the "figure" space
    plt.show()

elif(df1=="B"):
    print("Enter the ID of the pokemon")
    ID = int(input())
    tt = data[:].where(data['id']==ID)
    idx1 = tt.index[tt['id']==ID]
    qt = tt[tt['id'].notnull()]
    for i in qt.columns:
        print(i," : ",qt[i][idx1[0]])
    plt.imshow(imag[idx1[0]])
    plt.axis("off")   # turns off axes
    plt.axis("tight")  # gets rid of white border
    plt.axis("image")  # square up the image instead of filling the "figure" space
    plt.show()

