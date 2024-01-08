export lua=lua-5.4.6
if [ ! -d lua ]; then
    tar -xf $lua.tar.gz && mv $lua lua
fi
cd lua
make mingw

cd ..
scons.bat