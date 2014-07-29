#!/bin/bash

# hard code
#qt='Luxcoin-Qt.app'
#qtpro='luxcoin-qt.pro'
#qtproc='Luxcoin-Qt'
#name='luxcoin'
#logo='luxcoin.jpeg'
#dmg='LuxWallet.dmg'

# make sure coin name is input
#   for automation, pass coin name as variable 1 (e.g. ./script coinname)
if [[ -n "$1" ]]; then
    name=$1
else
    printf "Enter name of coin (e.g. luxcoin)\n> "
    read name
fi

echo "Make sure logo is of the form 'coinname.jpeg'"

# ensure letter case has correct formatting
name_lc=$(echo $name | tr '[:upper:]' '[:lower:]')
logo=${name_lc}'.jpeg'
dmg=$(echo ${name_lc:0:1} | tr '[:lower:]' '[:upper:]')${name_lc:1}'Wallet.dmg'
qtpro=${name_lc}'-qt.pro'
qt=$(echo ${name_lc:0:1} | tr '[:lower:]' '[:upper:]')${name_lc:1}'-Qt.app'
qtproc=$(echo ${name_lc:0:1} | tr '[:lower:]' '[:upper:]')${name_lc:1}'Qt'


# make custom logos
sips -z 256 256 -s format icns ${logo} --out ${name}/src/qt/res/icons/bitcoin.icns

sips -s format png ${logo} --out ${name}/src/qt/res/icons/bitcoin.png

sips -s format png ${logo} --out ${name}/src/qt/res/icons/toolbar_testnet.png

sips -s format png ${logo} --out ${name}/src/qt/res/icons/toolbar.png

cp ${logo} ${name}/src/qt/res/images/splash2.jpg

cd ${name}
qmake "USE_UPNP=-" ${qtpro}

make -f Makefile

sudo macdeployqt ${qt}

echo "Installing libdb_cxx-4.8.dylib by cyberhand. . ."
sudo cp ../libdb_cxx-4.8.dylib ${qt}/Contents/Frameworks

sudo install_name_tool -id @executable_path/../Frameworks/libdb_cxx-4.8.dylib ${qt}/Contents/Frameworks/libdb_cxx-4.8.dylib

sudo install_name_tool -change /opt/local/lib/db48/libdb_cxx-4.8.dylib @executable_path/../Frameworks/libdb_cxx-4.8.dylib ${qt}/Contents/MacOs/${qtproc}

echo 'Writing DMG sir. . .'
sudo hdiutil create -format UDBZ -quiet -srcfolder ${qt} ${dmg}
echo Done
