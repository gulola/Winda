imie=raw_input("Jak masz na imie?")

smietex=["Patryk", "Patrycja"]
if (imie in smietex):
    print"Radz se sam, Stany sa pelne pieknych mozliwosci!"
elif (imie=="Jacek"):
    print "Masz dwie rozne skarpetki, wypad stont."
elif (imie!=smietex):
    europa=int(raw_input("Na jakie pietro chcesz jechac?"))
    glupiestany=str(europa+1)
    print "Pacz pan, a w glupich Stanach to", glupiestany+". pietro!"