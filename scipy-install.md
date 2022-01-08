/opt/homebrew/bin/brew install openblas
export OPENBLAS=$(/opt/homebrew/bin/brew --prefix openblas)
export CFLAGS="-falign-functions=8 ${CFLAGS}"
git clone https://github.com/scipy/scipy.git
cd scipy
git submodule update --init
/opt/homebrew/bin/pip3 install .
/opt/homebrew/bin/pip3 install scikit-learn