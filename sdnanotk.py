import tkinter as tk
import tkinter.ttk as ttk
import customtkinter as ctk
import torch
import time
from PIL import ImageTk
from authtoken import auth_token
from torch import autocast
from diffusers import StableDiffusionPipeline

app = tk.Tk()
app.geometry("532x632")
app.title("SD nano TK")
ctk.set_appearance_mode("dark")
big_frame = ttk.Frame(app)
big_frame.pack(fill="both", expand=True)
style = ttk.Style(app)
app.tk.call("source", "azure.tcl")
app.tk.call("set_theme", "dark")

prompt = ctk.CTkEntry(height=40, width=512, text_color="black", fg_color="white", master=app)
prompt.place(x=10, y=10)

lmain = ctk.CTkLabel(height=512, width=512, master=app, text="")
lmain.place(x=10, y=110)

modelid = "CompVis/stable-diffusion-v1-4"
device = "cuda"
pipe = StableDiffusionPipeline.from_pretrained(modelid, revision="fp16", torch_dtype=torch.float16, use_auth_token=auth_token)
pipe.enable_attention_slicing()
pipe.safety_checker = None
pipe.to(device)
pipe.enable_sequential_cpu_offload()
pipe.enable_xformers_memory_efficient_attention()

def generate():
    with autocast(device):
        image = pipe(prompt.get(), guidance_scale=8.5).images[0]

    image.save(time.strftime("%Y%m%d-%H%M%S")+'.png')
    img = ImageTk.PhotoImage(image)
    lmain.configure(image=img)

trigger = ctk.CTkButton(height=40, width=120, text_color="white", fg_color="blue", command=generate, master=app)
trigger.configure(text="Go")
trigger.place(x=206, y=60)

app.mainloop()