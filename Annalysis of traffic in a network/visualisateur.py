list_IP = []
tab_trames = []
filtre = ""
protocole = ""
adr_ip = ""
adr_src = ""
adr_dst = ""
ihl = 0
thl = 0
lent = 0
dic = dict()
visualisation_fichier = open("visualisation.puml", "w")


def isHTTP(octets):
    try:
        debut_http = int(octets[4 * ihl + thl * 4 + 14], 16)
        if debut_http > 15:
            global lent
            lent = len(octets[4 * ihl + thl * 4 + 13: -1])
            return True
        else: return False
    except:
        return False



def tcp(octets):

    port_src = int(octets[14+4*ihl]+octets[15+4*ihl], 16)
    port_dst = int(octets[16+4*ihl]+octets[17+4*ihl], 16)
    nseq = int(octets[18+4*ihl]+octets[19+4*ihl]+octets[20+4*ihl]+octets[21+4*ihl], 16)
    ackn = int(octets[22+4*ihl]+octets[23+4*ihl]+octets[24+4*ihl]+octets[25+4*ihl], 16)
    global thl
    thl = int(octets[4*ihl + 26][0], 16)

    flags_set = []
    reserved = (int(octets[ihl*4 + 26][1], 16) & 14) >> 1
    if reserved !=0: flags_set.append('Reserved')
    accurate_ecn = int(octets[ihl*4 + 26][1], 16) & 1
    if accurate_ecn !=0: flags_set.append('Accurate ECN')
    cwr = (int(octets[ihl*4 + 27][0], 16) & 8) >> 3
    if cwr !=0: flags_set.append('Congestion window reduced')
    ecn_echo = (int(octets[ihl*4 + 27][0], 16) & 4) >> 2
    if ecn_echo !=0: flags_set.append('ECN Echo')
    urgent = (int(octets[ihl*4 + 27][0], 16) & 2) >> 1
    if urgent !=0: flags_set.append('Urgent')
    acks = (int(octets[ihl*4 + 27][0], 16) & 1)
    if acks !=0: flags_set.append('ACK')
    push = (int(octets[ihl*4 + 27][1], 16) & 8) >> 3
    if push !=0: flags_set.append('Push')
    reset = (int(octets[ihl*4 + 27][1], 16) & 4) >> 2
    if reset !=0: flags_set.append('Reset')
    syn = (int(octets[ihl*4 + 27][1], 16) & 2) >> 1
    if syn !=0: flags_set.append('SYN')
    fin = (int(octets[ihl*4 + 27][1], 16) & 1)
    if fin !=0: flags_set.append('FIN')

    window = int(octets[ihl*4 + 28] + octets[ihl*4 + 29], 16)
    #print (window)

    if isHTTP(octets) and (filtre != "oui" or protocole == "http" or protocole == "HTTP" or protocole == "tcp" or protocole == "TCP" or adr_ip == adr_src or adr_ip == adr_dst):
        if not adr_src in list_IP:
            list_IP.append(adr_src)
        if not adr_dst in list_IP:
            list_IP.append(adr_dst)

        list_http = ''.join(octets[4 * ihl + thl * 4 + 14:-1])

        ligneshttp = []
        for l in list_http.split('0d0a'):
            try:
                ligneshttp.append(bytearray.fromhex(l).decode())
            except:
                continue

        echange = []
        echange.append(adr_src)
        echange.append(adr_dst)
        ch = "HTTP:  " + str(ligneshttp[0]) + " "
        try:
            for y in ligneshttp:
                yy=y.split()
                if yy[0] == 'Content-Type:':
                    ch+= str(yy[1])
        except:
            pass

        echange.append(ch)
        tab_trames.append(echange)

    elif filtre != "oui" or protocole == "tcp" or protocole == "TCP" or adr_ip == adr_src or adr_ip == adr_dst:
        if not adr_src in list_IP:
            list_IP.append(adr_src)
        if not adr_dst in list_IP:
            list_IP.append(adr_dst)

        echange = []
        echange.append(adr_src)
        echange.append(adr_dst)

        global dic
        if port_src not in dic.keys():
            seqack = []
            seqack.append(nseq)
            seqack.append(ackn)
            if ackn == 0: ackn-=1
            dic.update({port_src: seqack})

        ch = "TCP: " + str(port_src) + " -> " +str(port_dst) + " "
        if flags_set:
            ch += str(flags_set)
        ch += " seq=" + str(nseq-dic[port_src][0])
        if (ackn-dic[port_src][1]+1) != 0:
            if dic[port_src][1]==0: dic[port_src][1]=ackn
            ch+= " Ack="+str(ackn-dic[port_src][1]+1)
        ch+= " Win=" + str(window) + " len=" + str(lent)
        echange.append(ch)
        tab_trames.append(echange)



def ip(octets):
    global ihl
    ihl = int(octets[14].strip()[1], 16)
    global adr_src
    adr_src = '.'.join([str(int(i, 16)) for i in octets[26:30]])
    global adr_dst
    adr_dst= '.'.join([str(int(i, 16)) for i in octets[30:34]])

    if (int(octets[23], 16) == 6):
        tcp(octets)
    else : print("protocole unsupporté")



def traitement(trame):
    if trame[12] + trame[13] == "0800":
        ip(trame)
    else: print("Protocole unsopporté")

def parcourir_fichier(fichier):

    lignes = fichier.readlines()
    octets = []

    for i in range(len(lignes)):
        try:
            ligne = lignes[i].strip().lower()
            ligne = ligne.split(maxsplit=1)[1]
            ligne = ligne.split()
            for oct in range(16):
                try:
                    octets.append(ligne[oct])
                except:
                    pass
        except:
            #print(octets)
            traitement(octets)
            octets=[]


def generer_diagramme(fichier):
    for i in range(len(list_IP)):
        fichier.write("participant " + list_IP[i] + "\n")
    for i in range(len(tab_trames)):
        fichier.write(tab_trames[i][0] + " -> " + tab_trames[i][1] + " : " + tab_trames[i][2] + "\n")

def entree():
    global  filtre
    global  type
    global  protocole
    global  adr_ip
    filtre = input("Voulez vous appliquer un filtre (oui/non) : ")
    if filtre == "oui":
        type = input("Filtre par (protocole/adresse_ip) : ")
        while type != "protocole" and type != "adresse_ip":
            type = input("Veuillez entrer un type du filtre correcte (protocole/adresse_ip) : ")
        if type == "protocole":
            protocole = input("Entrer le nom du protocole : ")
            while protocole != "tcp" and protocole != "TCP" and protocole != "http" and protocole != "HTTP":
                protocole = input("Veuillez entrer un protocole supporté (TCP/HTTP) : ")
                print(protocole)
        elif type == "adresse_ip":
            adr_ip = input("Entrer l'adresse IP : ")

def main():
    try:
        f = input("Entrer le fichier a traite : ")
        fichier = open(f)
        entree()
    except:
        print("Erreur: Le fichier n'existe pas ")

    visualisation_fichier.write("@startuml \n")
    parcourir_fichier(fichier)
    generer_diagramme(visualisation_fichier)
    visualisation_fichier.write("@enduml \n")
    visualisation_fichier.close()

if __name__ == "__main__":
    main()