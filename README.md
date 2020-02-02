# INSTALLING FAN SHIM
git clone https://github.com/pimoroni/fanshim-python

cd fanshim-python

sudo ./install.sh

cd examples

sudo ./install-service.sh --on-threshold 65 --off-threshold 55 --delay 2

# STOPPING SERVICE 
sudo systemctl stop pimoroni-fanshim.service

# CONFIGURING SERVICE
sudo systemctl stop pimoroni-fanshim.service

sudo ./install-service.sh --on-threshold 75 --off-threshold 60 --delay 5

# PERMAMENTLY DISABLE
sudo systemctl stop pimoroni-fanshim.service

sudo systemctl disable pimoroni-fanshim.service

# RE-ENABLE SERVICE
sudo systemctl enable pimoroni-fanshim.service

sudo systemctl start pimoroni-fanshim.service

# START TESTING
python3 temp_check.py

gcc -o cpuburn-a53 cpuburn-a53.S

./cpuburn-a53
