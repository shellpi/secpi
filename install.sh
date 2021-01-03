echo "Getting SecPi source..."
curl -L https://github.com/shellpi/secpi/archive/main.zip -o secpi.zip > /dev/null
unzip secpi.zip > /dev/null

echo "Installing dependencies..."
pip install -r secpi-main/requirements.txt > /dev/null

echo "Locating SecPi..."
mkdir /usr/secpi
cp secpi/bin/secpi /usr/secpi/
cp -r src /usr/secpi/
export PATH=$PATH:/usr/secpi


echo "SecPi installation complete"
