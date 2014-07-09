#!/bin/bash

#take args instead?
qt='Luxcoin-Qt.app'
qtpro='luxcoin-qt.pro'
qtproc='Luxcoin-Qt'
name='luxcoin'
logo='luxcoin.jpeg'
dmg='LuxWallet.dmg'

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
