import torch, time, gc, logging, cv2, os
from os import system, name
from authtoken import auth_token
from termcolor import colored
from torch import autocast
from diffusers.models import AutoencoderKL
from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler


def purge():
    torch.cuda.empty_cache()
    torch.cuda.ipc_collect()
    gc.collect()


def displayimage():
    print(colored("Displaying image, close image window to continue...", "light_red"))
    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    cv2.imshow(filename, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def generate(idevice, iprompt, inegative, isteps, iguidance):
    if not iprompt: iprompt = "face, very expressive, portrait photography, world photography, soft studio lighting, intricate, beautiful, award winning, stunning, stock film, 8k, centered, amazing, impressive, awesome, highly detailed, fantastic, overwhelming, masterpiece, subject in frame"
    if inegative == '!no': inegative = None
    elif not inegative: inegative = "ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, extra limbs, disfigured, deformed, body out of frame, bad anatomy, watermark, signature, cut off, low contrast, underexposed, overexposed, bad art, beginner, amateur, distorted face, artifacts, jpeg noise, bad eyes, text"
    if not isteps: isteps = 50
    if not iguidance: iguidance = 8.5
    with autocast(idevice):
        image = pipe(prompt=iprompt, guidance_scale=iguidance,
                     num_inference_steps=isteps, negative_prompt=inegative).images[0]
    inow = time.strftime("%Y%m%d-%H%M%S")
    ifilename = inow + '.png'
    image.save(ifilename)
    with open(inow + '.txt', 'w', encoding='utf-8') as f:
        f.write("Prompt   : " + str(iprompt) + "\n")
        f.write("Negative : " + str(inegative) + "\n")
        f.write("Steps    : " + str(isteps) + "\n")
        f.write("Guidance : " + str(iguidance) + "\n")
        f.write("Output   : " + str(ifilename) + "\n")
    f.close()
    return ifilename


logging.disable(logging.WARNING)
os.system('color')
modelid = "SG161222/Realistic_Vision_V2.0"
vaeid = "stabilityai/sd-vae-ft-mse"
device = "cuda"
print(colored("Loading " + modelid + "...", "white"))
vae = AutoencoderKL.from_pretrained(vaeid)
euler = EulerDiscreteScheduler.from_pretrained(modelid, subfolder="scheduler")
pipe = StableDiffusionPipeline.from_pretrained(modelid, torch_dtype=torch.float16, use_auth_token=auth_token,
                                               safety_checker=None, feature_extractor=None, use_safetensors=False,
                                               requires_safety_checker=False, scheduler=euler, vae=vae)
del pipe.vae.encoder
purge()
pipe.to(device)
pipe.enable_vae_tiling()
pipe.enable_attention_slicing("max")
pipe.enable_xformers_memory_efficient_attention(attention_op=None)
pipe.unet.to(memory_format=torch.channels_last)
pipe.enable_sequential_cpu_offload()
if name == 'nt': system('cls')
else: system('clear')
purge()
print(colored("\n\n\n############### SD NANO ###############", "cyan", attrs=["reverse", "bold"]))
print(colored("\nModel : " + modelid + "\nDevice: " + device + "\nVAE   : " + vaeid, "cyan"))
while True:
    prompt = input(colored("\nPrompt (!exit to quit, Enter for example): ", "light_green"))
    if prompt == '!exit': exit()
    negative = input(colored("Negative prompt (Enter for default, !no for none): ", "light_green"))
    steps = int(input(colored("Steps (Enter for 50): ", "light_green")) or 50)
    guidance = float(input(colored("Guidance scale (Enter for 8.5): ", "light_green")) or 8.5)
    display = input(colored("Display output to screen? (Y/n)", "light_green")).strip().lower()
    filename = generate(device, prompt, negative, steps, guidance)
    print("Done creating " + filename)
    purge()
    if not display or display.startswith("y"):
        displayimage()
        purge()

        
        
