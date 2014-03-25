#!/bin/sh
# Patching system files
cd /usr/lib/qt5/qml/Sailfish/Gallery
patch -p1 < /opt/SfietKonstantin/extensions/jolla-gallery/patchvideoposter.patch > /dev/null

cd /usr/share/jolla-gallery/pages
patch -p1 < /opt/SfietKonstantin/extensions/jolla-gallery/patchimageview.patch > /dev/null
exit 0
