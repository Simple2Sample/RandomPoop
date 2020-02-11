1. copy libfreenect.so.0.1.2 and libfreenect_sync.so.0.1.2 and libkinect_wrapper.so in /user/lib folder on your target.
2. copy the liblibusb.so.1.0.8 to /usr/local/lib 
3. create symbol link to these files by
=============================================================
#ln -s /usr/lib/libfreenect.so.0.1.2 /usr/lib/libfreenect.so.0.1
#ln -s /usr/lib/libfreenect_sync.so.0.1.2 /usr/lib/libfreenect_sync.so.0.1
#ln -s /usr/local/lib/liblibusb.so.1.0.8 /lib/libusb-1.0.so.0
=============================================================
