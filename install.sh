

sudo apt-get install libcurl4-gnutls-dev

git clone https://github.com/Cyan4973/lz4.git
cd lz4
make
sudo make install

cd ..

sudo apt-get install libjsoncpp-dev 

sudo apt-get install libboost-all-dev

git clone https://github.com/janelia-flyem/libdvid-cpp.git

cd libdvid-cpp

mkdir build 

cd build

cmake -DLIBDVID_WRAP_PYTHON=1 ..

make 

sudo make install

echo "export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib" >> ~/.bashrc

