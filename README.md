# sdnano
### Very small implementation of Stable Diffusion

Memory effecient and compact, can run decent SD models

Implements xformers, attention slicing, and sequential cpu offloading

**disables safety_checker**, be careful replacing the model

Can run inside **1.8 GB** of VRAM

(optional) You can create a virtual environment with:
```
python -m venv "venv"
venv\Scripts\activate
```

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

To use Realistic_Vision_V2.0 do: (https://huggingface.co/SG161222/Realistic_Vision_V2.0)
<br>
`python sdnanorv.py`

Not tested, do not use in production.
