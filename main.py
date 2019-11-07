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

            time.sleep(2)

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

            time.sleep(2)

if __name__ == "__main__":

    lijeva_dretva = DretvaLijeveCeste()
    desna_dretva = DretvaDesneCeste()
    gornja_dretva = DretvaGornjeCeste()
    donja_dretva = DretvaDonjeCeste()

    lijevo_desno_svijetlo = 1


    while True:

        if lijevo_desno_svijetlo == 1:


            if lijevi_brojac_auta < 5:
                lijevi_lock.acquire()
                lijevi_brojac_auta = 0
                lijevi_lock.release()

                print("Nema više auta lijevo!")

            else:
                lijevi_lock.acquire()
                lijevi_brojac_auta -= 5
                lijevi_lock.release()

                print("Lijevo je otišlo 5 autiju!")

            if desni_brojac_auta < 5:
                desni_lock.acquire()
                desni_brojac_auta = 0
                desni_lock.release()

                print("Nema više auta desno!")

            else:
                desni_lock.acquire()
                desni_brojac_auta -= 5
                desni_lock.release()

                print("Desno je otišlo 5 autiju!")

        time.sleep(10)


        lijevo_desno_svijetlo = 0

        if lijevo_desno_svijetlo == 0:

            if gornji_brojac_auta < 5:
                gornji_lock.acquire()
                gornji_brojac_auta = 0
                gornji_lock.release()

                print("Nema više auta gore!")

            else:
                gornji_lock.acquire()
                gornji_brojac_auta -= 5
                gornji_lock.release()

                print("Gore je otišlo 5 autiju!")

            if donji_brojac_auta < 5:
                donji_lock.acquire()
                donji_brojac_auta = 0
                donji_lock.release()

                print("Nema više auta dole!")

            else:
                donji_lock.acquire()
                donji_brojac_auta -= 5
                donji_lock.release()

                print("Dole je otišlo 5 autiju!")

        time.sleep(10)

        print("Lijevo: " + str(lijevi_brojac_auta) + " Desno: " + str(desni_brojac_auta))
        print("Gore: " + str(gornji_brojac_auta) + " Dole: " + str(donji_brojac_auta))

        time.sleep(4)

        lijevo_desno_svijetlo = 1