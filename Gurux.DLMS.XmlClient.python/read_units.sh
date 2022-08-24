cd /home/thabure/Downloads/Gurux.DLMS.Python/Gurux.DLMS.Client.Example.python/
python3 main.py -S /dev/ttyUSB0 -t Verbose -r sn -g "1.1.1.8.1.255:2"
echo "---------------------------- Sending to Server -------------------------------------"
python3 units.py