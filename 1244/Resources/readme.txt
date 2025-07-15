🎉 Limited-Time Offer: Get 50% OFF Your First Subscription
Pricing
new
Demo
Workflows
AI Generator
Premium
Tutorials
Affiliate
Creators Plan
Workflow to AI Generator
new
Free Launch
Workflows/Flux Kontext Image Editing with Lora
Flux Kontext Image Editing with Lora
Save it for me
Operate
@
fjdsfjefjk
07/02/2025
ComfyUI
Popular & HOT
Image Editing
Flux
LoRA
AI Influencer
1 / 8
Detailed Introduction

This workflow allows you to use the Flux Kontext model to edit your image. I have put a dozen lora, mainly style editing ones.

Example for changing hair colors :




Workflow presentation :

The workflow uses the Kontext Dev Model, you can upload different version like the FP8 directly into the diffusion_models folder by uploading the link from Hugginface.




Upload the images.




Write your prompt, you can also add loras with the Power Lora Loader node, exampe of included loras down below.

Initially the workflow resize the image to dimensions preferred by the model and if you use 2 images, it stiches them together and uses the size of the stiched images for the output, I put the get image size node with an empty latent image to take only the dimensions of the first image.

You can go back to let the workflow choose the Kontext preferred dimensions by replacing the link from the empty latent to from the VAE encode latent output to the latent_image of the ksampler.

You can also remove the link from the get image size  to the empty latent and put custom dimensions, although it messes with the output quality.







You're now ready to get to it !

Here are the example for the loras included in the workflow, you can add lora by uploading them in the lora folder, I also put a note node with the file name to load in the lora node and the prompt to use :

RealisticKontextLoRA

GuoHuaKontextLoRA

Ghibli Style

Kontext Pixel Art

FlatAnimteStyleV1

Kontext Three-view sketch

Dragon Ball Style

Glass Prism

Mech Anything

360 Degree

Kontext_change_clothes : didn't try putting a shirt on the cat.

UnFlux : didn't try it but it's supposed to help remove the flux style of flux generated images.

Fluffy Kontext Dev LoRA : the cat is already fluffy so it didn't show much changes :)










Details
APP
ComfyUI(v0.3.42)
Update Time
07/02/2025
File Space
3.1 GB
Models
13
Extensions
4
About This Template

Put the image, write your prompt, if you want lora check the note, click generate and here you go.

Navigation
Pricing
Demo
Workflows
AI Generator
Tutorials
Affiliate
Creators Plan
Workflow to AI Generator
About Us
Related terms
Terms of Service
Privacy Policy
Redeem Code
Cooperation
Contact Us
Payment Methods
© 2023-2025 Copyright by MimicPC™ All rights reserved