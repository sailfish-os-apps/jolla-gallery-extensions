#!/bin/sh
# Undoing patch
cd /usr/lib/qt5/qml/Sailfish/Gallery
patch -p1 < /opt/SfietKonstantin/extensions/jolla-gallery/unpatchvideoposter.patch > /dev/null

cd /usr/share/jolla-gallery/pages
patch -p1 < /opt/SfietKonstantin/extensions/jolla-gallery/unpatchimageview.patch > /dev/null
exit 0