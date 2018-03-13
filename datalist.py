nama = ['Ari','Bambang']
nilai = [80,90]

print("###########################")
print("| NO |   NAMA   |  NILAI  |")
print("###########################")
for i in range(len(nama)):
    #print("| %2 | %-11s | %5d |" % (i+1,nama [i],nilai[i]))
    print ("| {no:2d} |{nama:11s}|{nilai:5.2f}   |".format(nama=nama[1],nilai=nilai[i],
    no=i+1))

print ("###########################")
    
