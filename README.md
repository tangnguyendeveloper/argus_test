# ARGUS TESTING

Author: **Tang Nguyen-Tan**  
Email: [tangnt.1289@gmail.com](mailto:tangnt.1289@gmail.com)

---

## Test Environment

- Python 3.12
- Ubuntu 24.04 LTS Server

---

## Installation

```bash
# Switch to root mode
su -m

# Create and activate a Python virtual environment
python3 -m venv ./lo_evnv
source lo_evnv/bin/activate

# Install Python dependencies
pip install pandas

# Update system packages and install required libraries
apt update
apt-get install -y build-essential flex bison libpcap-dev libssl-dev libtirpc-dev wget git

# Download and build Argus server
wget https://github.com/openargus/argus/archive/refs/tags/v5.0.2.tar.gz
tar -xvzf v5.0.2.tar.gz
cd argus-5.0.2/
CFLAGS="-fstack-protector-strong -D_FORTIFY_SOURCE=2 -O2" ./configure
make -j$(nproc)
make install

# Go back and build Argus clients
cd ..
wget https://github.com/openargus/clients/archive/refs/tags/v5.0.0.tar.gz
tar -xvzf v5.0.0.tar.gz
cd clients-5.0.0/
./configure
make -j$(nproc)
make install
