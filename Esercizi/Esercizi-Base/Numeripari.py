def numeripari (parametro):
    Playlist=[]
    for i in range (2,eta+1,2):
        Playlist.append(i)
    return Playlist
eta=int(input("Inserisci l'età"))
print(f"L'età inserita è {eta}")
if eta>=18:
    print("Sei una maggiorenne ")
else:
    print("Sei una minorenne!")
Borghelist=numeripari(eta)
for element in Borghelist :
    print(element,end=" ")
a=0
print(" ")
while a<len(Borghelist):
    print(Borghelist[a])
    a+=1
a=0
while True:
    print(Borghelist[a])
    a=a+1
    if a==2:
        break