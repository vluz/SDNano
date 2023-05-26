import torch
import time
import streamlit as st
from authtoken import auth_token
from torch import autocast
from diffusers import StableDiffusionPipeline


def generate(prompt):
    with autocast(device):
        image = pipe(prompt, guidance_scale=8.5).images[0]

    image.save(time.strftime("%Y%m%d-%H%M%S")+'.png')
    st.image(image)


st.write("""# SD nano WEB""")
modelid = "CompVis/stable-diffusion-v1-4"
device = "cuda"
pipe = StableDiffusionPipeline.from_pretrained(modelid, revision="fp16", torch_dtype=torch.float16, use_auth_token=auth_token)
pipe.enable_attention_slicing()
pipe.to(device)
pipe.enable_sequential_cpu_offload()
pipe.enable_xformers_memory_efficient_attention()
prompt = st.text_input("Prompt: ")
if st.button('Go'): generate(prompt)