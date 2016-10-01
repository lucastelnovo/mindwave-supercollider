echo Please put device in pairing mode before using this autoconnect tool
echo Killing serial connection 0
sudo rfcomm release 0
echo Restarting bluetooth
sudo systemctl stop bluetooth
sudo systemctl start bluetooth
echo Wait for bluetooth to finish initializing
sleep 1
echo Scanning for address
ADDRESS=$(echo -e "power on\agent on\nquit\n" | bluetoothctl | grep -i mindwave | cut -f4 -s -d \ )
echo Pairing using address: $ADDRESS
echo -e "power on\nagent on\npair $ADDRESS\nquit" | bluetoothctl
echo Binding to serial port 0. Make sure the user is added to group uucp.
sudo rfcomm bind 0 $ADDRESS


