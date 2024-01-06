export lua=lua-5.4.6

tar -xf $lua.tar.gz && mv $lua lua
cd lua

make mingw