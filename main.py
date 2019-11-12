import threading
import time
from random import randint

lijevi_brojac_auta = 0
desni_brojac_auta = 0
gornji_brojac_auta = 0
donji_brojac_auta = 0

lijevi_lock = threading.Lock()
desni_lock = threading.Lock()
gornji_lock = threading.Lock()
donji_lock = threading.Lock()

class DretvaLijeveCeste():

    def __init__(self, interval = 1):
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):

        global  lijevi_brojac_auta
        while True:
            flag = randint(0,3)

            if flag == 0 or flag == 1:

                lijevi_lock.acquire()
                lijevi_brojac_auta += 1
                lijevi_lock.release()
                print("Lijevo -> " + str(lijevi_brojac_auta))

            time.sleep(2)

class DretvaDesneCeste():

    def __init__(self, interval = 1):
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):

        global  desni_brojac_auta
        while True:
            flag = randint(0,3)

            if flag == 0 or flag == 1:
                desni_lock.acquire()
                desni_brojac_auta += 1
                desni_lock.release()

                print("Desno -> " + str(desni_brojac_auta))

            time.sleep(2)

class DretvaGornjeCeste():

    def __init__(self, interval = 1):
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):

        global  gornji_brojac_auta
        while True:
            flag = randint(0,3)

            if flag == 0 or flag == 1:

                gornji_lock.acquire()
                gornji_brojac_auta += 1
                gornji_lock.release()
                print("Gore -> " + str(gornji_brojac_auta))

            time.sleep(1)

class DretvaDonjeCeste():

    def __init__(self, interval = 1):
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):

        global  donji_brojac_auta
        while True:
            flag = randint(0,3)

            if flag == 0 or flag == 1:

                donji_lock.acquire()
                donji_brojac_auta += 1
                donji_lock.release()
                print("Dole -> " + str(donji_brojac_auta))

            time.sleep(1)


def izracunajPropusnost(maxPropusti,minPropusti):

    maxLijevoDesno = max(lijevi_brojac_auta, desni_brojac_auta)
    maxGoreDole = max(gornji_brojac_auta, donji_brojac_auta)

    propustiLijevoDesno = 0;
    propustiGoreDolje = 0;
    koeficijentOdnosaSmjerova = 1;
    if maxLijevoDesno > 0 and maxGoreDole > 0:
        if maxLijevoDesno >= maxGoreDole:
            koeficijentOdnosaSmjerova = maxLijevoDesno / maxGoreDole
            propustiLijevoDesno = int(koeficijentOdnosaSmjerova * (minPropusti))

            if propustiLijevoDesno > maxPropusti:
                propustiLijevoDesno = maxPropusti
            propustiGoreDolje = minPropusti;

        elif maxGoreDole > maxLijevoDesno:
            koeficijentOdnosaSmjerova = maxGoreDole / maxLijevoDesno
            propustiGoreDolje = int(koeficijentOdnosaSmjerova * (minPropusti))

            if propustiGoreDolje > maxPropusti:
                propustiGoreDolje = maxPropusti

            propustiLijevoDesno = minPropusti;
    elif maxLijevoDesno == 0 and maxGoreDole > 0:
        propustiGoreDolje = maxPropusti;
    elif maxGoreDole == 0 and maxLijevoDesno > 0:
        propustiLijevoDesno = maxPropusti;

    return [propustiLijevoDesno, propustiGoreDolje]


if __name__ == "__main__":

    lijeva_dretva = DretvaLijeveCeste()
    desna_dretva = DretvaDesneCeste()
    gornja_dretva = DretvaGornjeCeste()
    donja_dretva = DretvaDonjeCeste()

    maxPropusti = 25
    minPropusti = 5

    lijevo_desno_svijetlo = 1


    while True:

        if lijevo_desno_svijetlo == 1:

            lijevi_lock.acquire()
            desni_lock.acquire()
            gornji_lock.acquire()
            donji_lock.acquire()

            propustiLijevoDesno = izracunajPropusnost(maxPropusti, minPropusti)[0]

            print("Palim zeleno u smjeru lijevo <-> desno")
            print("Lijevo: " + str(lijevi_brojac_auta) + " Desno: " + str(desni_brojac_auta))
            print("Gore: " + str(gornji_brojac_auta) + " Dole: " + str(donji_brojac_auta))

            if lijevi_brojac_auta > propustiLijevoDesno:
                lijevi_brojac_auta -= propustiLijevoDesno
                print("Lijevo je otišlo " + str(propustiLijevoDesno) +" autiju!")
            else:
                print("Lijevo je otišlo " + str(lijevi_brojac_auta) + " autiju!")
                lijevi_brojac_auta = 0
                print("Nema više auta lijevo!")

            if desni_brojac_auta > propustiLijevoDesno:
                desni_brojac_auta -= propustiLijevoDesno
                print("Desno je otišlo " + str(propustiLijevoDesno) + " autiju!")
            else:
                print("Desno je otišlo " + str(desni_brojac_auta) + " autiju!")
                desni_brojac_auta = 0
                print("Nema više auta desno!")

            lijevi_lock.release()
            desni_lock.release()
            gornji_lock.release()
            donji_lock.release()
            print("Palim crveno u smjeru lijevo <-> desno")

        time.sleep(10)

        lijevo_desno_svijetlo = 0

        if lijevo_desno_svijetlo == 0:

            lijevi_lock.acquire()
            desni_lock.acquire()
            gornji_lock.acquire()
            donji_lock.acquire()

            propustiGoreDole = izracunajPropusnost(maxPropusti, minPropusti)[1]

            print("Palim zeleno u smjeru gore <-> dolje")
            print("Lijevo: " + str(lijevi_brojac_auta) + " Desno: " + str(desni_brojac_auta))
            print("Gore: " + str(gornji_brojac_auta) + " Dole: " + str(donji_brojac_auta))

            if gornji_brojac_auta > propustiGoreDole:
                gornji_brojac_auta -= propustiGoreDole
                print("Gore je otišlo " + str(propustiGoreDole) +" autiju!")
            else:
                print("Gore je otišlo " + str(gornji_brojac_auta) + " autiju!")
                gornji_brojac_auta = 0
                print("Nema više auta gore!")

            if donji_brojac_auta > propustiGoreDole:
                donji_brojac_auta -= propustiGoreDole
                print("Dolje je otišlo " + str(propustiGoreDole) +" autiju!")
            else:
                print("Dolje je otišlo " + str(donji_brojac_auta) + " autiju!")
                donji_brojac_auta = 0
                print("Nema više auta dolje!")

            lijevi_lock.release()
            desni_lock.release()
            gornji_lock.release()
            donji_lock.release()
            print("Palim crveno u smjeru gore <-> dolje")

        time.sleep(10)

        #print("Lijevo: " + str(lijevi_brojac_auta) + " Desno: " + str(desni_brojac_auta))
        #print("Gore: " + str(gornji_brojac_auta) + " Dole: " + str(donji_brojac_auta))

        lijevo_desno_svijetlo = 1
