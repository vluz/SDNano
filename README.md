# sdnano
### Very small implementation of Stable Diffusion that is still useful

Memory effecient and compact, can run decent SD models

Implements xformers, attention slicing, and sequential cpu offloading

**disables safety_checker**, be careful replacing the model

Can run inside **1.8 GB** of VRAM

Tested with **Python 3.10.6**

Uses Azure ttk dark theme (https://github.com/rdbende/Azure-ttk-theme)

Require HuggingFace Security token in file `authtoken.py`, can be gotten freely, details at:
<br>
https://huggingface.co/docs/hub/security-tokens

<hr>

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

With RV2 and this example prompt from the model developper: <br>
*RAW photo, a close up portrait photo of 26 y.o woman in wastelander clothes, long haircut, pale skin, slim body, background is city ruins, (high detailed skin:1.2), 8k uhd, dslr, soft lighting, high quality, film grain, Fujifilm XT3*<br>
Result:<br>
![Generation result](20230527-095756.png?raw=true "Result")


Not fully tested, use in production at your own risk.
