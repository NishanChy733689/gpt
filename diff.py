from diffusers import DiffusionPipeline

pipe = DiffusionPipeline.from_pretrained("sd-legacy/stable-diffusion-v1-5")
pipe.load_lora_weights("maria26/Floor_Plan_LoRA")

prompt = "Floor plan of a 1300 square foot apartment, few bedrooms, one bathroom, big kitchen, many windows, a study room and a guestroom"
image = pipe(prompt).images[0]