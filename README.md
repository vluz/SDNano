# sdnano
### Very small implementation of Stable Diffusion

Memoty effecient and compact implementation of Stable Diffusion

Implements xformers, attention slicing and sequential cpu offloading

Can run inside 2GB of VRAM

To install do:
```
git clone https://github.com/vluz/sdnano.git
cd sdnano
pip install -r requirements.txt
```

To run do:<br>
`python sdnano.py` for the cli version
<br>or
`python sdnanotk.py` for the TK version
<br>or
`streamlit run sdnanoweb.py` for the streamlit version

Not tested, do not use in production.
