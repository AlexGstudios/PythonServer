import socket
def getHostIp(adress):
    ad = str(adress[0])
    addr = socket.gethostbyname(ad)
    return addr

#tryck ner en knapp på produkten, startar bluetooth på rasp pi
#sammankoppla mobilen och rasp pi
#gå in på appen/inställningar
#lägg till en "slot" klicka på "slot'en" och klicka uppdatera
#
#kod bakom som skickar en request från mobil till rasp pi
#Rasp pi skickar sin ip
#"slot'en" uppdateras med rasp pi ip