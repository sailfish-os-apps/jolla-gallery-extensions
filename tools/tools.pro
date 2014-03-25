TEMPLATE = subdirs
OTHER_FILES = post.sh \
    preun.sh \
    patchimageview.patch \
    patchvideoposter.patch \
    unpatchimageview.patch \
    unpatchvideoposter.patch
    

patch.files += $$OTHER_FILES
patch.path +=  /opt/SfietKonstantin/extensions/jolla-gallery
INSTALLS += patch
