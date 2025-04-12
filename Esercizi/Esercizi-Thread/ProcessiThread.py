import threading                                                                    #Per creare i thread
import multiprocessing                                                              #Per creare i processi
import time                                                                         #Per il tempo
import random                                                                       #Per generare numeri casuali

#Funzione per la creazione dei thread

def generaNumeri(nome):
    print(f"Sto iniziando il thread {nome}")                                        #Stampa il nome del thread
    i = 0 
    while i < 100:                                                                  #Ciclo per generare 100 numeri
        print(f"{nome}-Ho generato il numero  {random.randint(0, 100)}")
        i += 1
        time.sleep(2)                                                               #Aspetta 2 secondo
        print (f" Ho finito il thread ")

def main():     
    print(f"Inizio dello script")       
    inizio = time.time()                                                            #Inizio del tempo
    t1 = threading.Thread(target=generaNumeri, args=("t1",))                         #Creo un thread
    t2 = threading.Thread(target=generaNumeri, args=("t2",))                         #Creo un altro thread
    
    p1=multiprocessing.Process(target=generaNumeri, args=("p1",))                    #Creo un processo
    p2=multiprocessing.Process(target=generaNumeri, args=("p2",))                    #Creo un altro processo
    
    t1.start()                                                                      #Avvio il thread
    t2.start()                                                                      #Avvio il secondo thread
    
    p1.start()                                                                      #Avvio il processo
    p2.start()                                                                      #Avvio il secondo processo
    
    t1.join()                                                                       #Aspetto che il thread finisca
    t2.join()                                                                       #Aspetto che il secondo thread finisca
    
    p1.join()                                                                      #Aspetto che il processo finisca
    p2.join()                                                                      #Aspetto che il secondo processo finisca



    #generaNumeri()                                                                 #Avvio la funzione generaNumeri
    #generaNumeri()                                                                 #Avvio la funzione generaNumeri
    
    #time.sleep(2)                                                                  #Aspetta 2 secondo
    
    
    #Scrivo delle istruzioni
    fine = time.time()                                                              #Fine del tempo
    print(f"Tempo di esecuzione {fine - inizio:.2f} secondi")


if __name__ == "__main__":
    main()
