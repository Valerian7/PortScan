from concurrent.futures import ThreadPoolExecutor
import socket
import sys,getopt

def scan(ip,port):
    s = socket.socket()
    s.settimeout(0.1)
    protocolname = 'tcp'
    if s.connect_ex((ip,port)) == 0:   
        try:
            print("端口%4d开启：%s" %(port,socket.getservbyport(port,protocolname)))
        except:
            print('端口%4d开启: Unknown '%port)
    s.close()
    

def main(argv):
    host = ''
    start = ''
    end = ''
    try:
        opts,args = getopt.getopt(argv,"hi:s:d:",["host=","start=","end="])
    except getopt.GetoptError:
        print ('PortScan.py -i <host> -s <start> -d <end>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == ("-h"):
            print ('PortScan.py -i <host> -s <port_start> -d <port_end>')
            sys.exit()
        elif opt in ("-i", "--host"):
            host = arg
        elif opt in ("-s", "--start"):
            start = int(arg)
        elif opt in ("-d", "--end"):
            end = int(arg)

    print ('ip为：', host ,"\n")
    print (f"端口范围 ：{start}-{end} \n")
    with ThreadPoolExecutor(100) as f:
        for port in range(start,end): 
            f.submit(scan,host,port)
    print("扫描已完成")
            
if __name__ == "__main__":
   main(sys.argv[1:])
