# sdnano
### **Update:** Please use `sdnanorv.py` for any generation. 
The remaining implementations are reference and of smaller size for classes use.

<hr>

### Very small implementation of Stable Diffusion that is still useful

Memory effecient and compact, can run decent SD models

Implements xformers, attention slicing, and sequential cpu offloading

**disables safety_checker**, be careful replacing the model

Can run inside **1.2 GB** of VRAM

Tested with **Python 3.10.6**

Uses Azure ttk dark theme (https://github.com/rdbende/Azure-ttk-theme)

<hr>

➡️Requires Hugging Face Security token in file `authtoken.py`, can be gotten freely, details at:
<br>
https://huggingface.co/docs/hub/security-tokens

Open a command prompt and `cd` to a new directory of your choosing:

(optional; recommended) Create a virtual environment with:
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

On first run it will download several models from Hugging Face.
<br>
It will take quite some time, please let it finish.

To run do:<br>
➡️**`python sdnanorv.py` for the fully functional cli version**
<br>
<br>or<br>
`python sdnano.py` for the reference cli version
<br>or<br>
`python sdnanotk.py` for the reference TK version
<br>or<br>
`streamlit run sdnanoweb.py` for the reference streamlit version

rv stands for Realistic_Vision_V2.0 (https://huggingface.co/SG161222/Realistic_Vision_V2.0)
<br>

With RV2 and this example prompt from the model developper: <br>
*RAW photo, a close up portrait photo of 26 y.o woman in wastelander clothes, long haircut, pale skin, slim body, background is city ruins, (high detailed skin:1.2), 8k uhd, dslr, soft lighting, high quality, film grain, Fujifilm XT3*<br>
Result:<br>
![Generation result](20230527-095756.png?raw=true "Result")


Not fully tested, use in production at your own risk.
