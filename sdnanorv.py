import torch
import time
from authtoken import auth_token
from torch import autocast
from diffusers import StableDiffusionPipeline


def generate(prompt):
    with autocast(device):
        image = pipe(prompt, guidance_scale=8.5).images[0]
    filename = time.strftime("%Y%m%d-%H%M%S")+'.png'
    image.save(filename)
    return filename


modelid = "SG161222/Realistic_Vision_V2.0"
device = "cuda"
pipe = StableDiffusionPipeline.from_pretrained(modelid, torch_dtype=torch.float16, use_auth_token=auth_token)
pipe.enable_attention_slicing()
pipe.safety_checker = None
pipe.to(device)
pipe.enable_sequential_cpu_offload()
pipe.enable_xformers_memory_efficient_attention()
print("\n\n\nSD nano")
prompt = input("Prompt: ")
filename = generate(prompt)
print("Done creating "+filename+"\n")