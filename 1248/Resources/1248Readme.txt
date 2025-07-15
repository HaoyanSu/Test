ComfyUI home page
Search...
Ctrl K

Get Started

Get Started
Introduction
Installation
Getting Started
Changelog
Basic Concepts
Workflow
Nodes
Custom Nodes
Properties
Links
Models
Dependencies
Interface Guide
Interface Overview
Mask Editor
ComfyUI Settings
Tutorials
Basic Examples
ControlNet
Flux
Image
3D
Video
LTX-Video
Hunyuan Video
Wan Video
Cosmos
Cosmos-Predict2
Audio
API Nodes
Troubleshooting
Overview
Model Issues
Custom Node Issues
Community
Contributing

English

Cosmos
Cosmos Predict2 Video2World ComfyUI Official Example

This guide demonstrates how to complete Cosmos-Predict2 Video2World workflows in ComfyUI

Cosmos-Predict2 is NVIDIA’s next-generation physical world foundation model, specifically designed for high-quality visual generation and prediction tasks in physical AI scenarios. The model features exceptional physical accuracy, environmental interactivity, and detail reproduction capabilities, enabling realistic simulation of complex physical phenomena and dynamic scenes.

Cosmos-Predict2 supports various generation methods including Text-to-Image (Text2Image) and Video-to-World (Video2World), and is widely used in industrial simulation, autonomous driving, urban planning, scientific research, and other fields. It serves as a crucial foundational tool for promoting deep integration of intelligent vision and the physical world.

GitHub:Cosmos-predict2 huggingface: Cosmos-Predict2

This guide will walk you through completing Video2World generation in ComfyUI.

For the text-to-image section, please refer to the following part:

Cosmos Predict2 Text to Image

Using Cosmos-Predict2 for text-to-image generation

If you find missing nodes when loading the workflow file below, it may be due to the following situations:

You are not using the latest Development (Nightly) version of ComfyUI.
You are using the Stable (Release) version or Desktop version of ComfyUI (which does not include the latest feature updates).
You are using the latest Commit version of ComfyUI, but some nodes failed to import during startup.

Please make sure you have successfully updated ComfyUI to the latest Development (Nightly) version. See: How to Update ComfyUI section to learn how to update ComfyUI.

​
Cosmos Predict2 Video2World Workflow

When testing the 2B version, it takes around 16GB VRAM.

​
1. Workflow File

Please download the video below and drag it into ComfyUI to load the workflow. The workflow already has embedded model download links.

Download Json Format Workflow File

Please download the following image as input:

​
2. Manual Model Installation

If the model download wasn’t successful, you can try to download them manually by yourself in this section.

Diffusion model

cosmos_predict2_2B_video2world_480p_16fps.safetensors

For other weights, please visit Cosmos_Predict2_repackaged to download

Text encoder

oldt5_xxl_fp8_e4m3fn_scaled.safetensors

VAE

wan_2.1_vae.safetensors

File Storage Location

Copy
Ask AI
📂 ComfyUI/
├──📂 models/
│   ├── 📂 diffusion_models/
│   │   └─── cosmos_predict2_2B_video2world_480p_16fps.safetensors
│   ├── 📂 text_encoders/
│   │   └─── oldt5_xxl_fp8_e4m3fn_scaled.safetensors
│   └── 📂 vae/
│       └──  wan_2.1_vae.safetensors

​
3. Complete Workflow  Step by Step

Please follow the steps in the image to run the workflow:

Ensure the Load Diffusion Model node has loaded cosmos_predict2_2B_video2world_480p_16fps.safetensors
Ensure the Load CLIP node has loaded oldt5_xxl_fp8_e4m3fn_scaled.safetensors
Ensure the Load VAE node has loaded wan_2.1_vae.safetensors
Upload the provided input image in the Load Image node
(Optional) If you need first and last frame control, use the shortcut Ctrl(cmd) + B to enable last frame input
(Optional) You can modify the prompts in the ClipTextEncode node
(Optional) Modify the size and frame count in the CosmosPredict2ImageToVideoLatent node
Click the Run button or use the shortcut Ctrl(cmd) + Enter to run the workflow
Once generation is complete, the video will automatically save to the ComfyUI/output/ directory, you can also preview it in the save video node

Was this page helpful?

Yes
No
Suggest edits
Previous
ACE-Step Music Generation
This guide will help you create dynamic music using the ACE-Step model in ComfyUI
Next
On this page
Cosmos Predict2 Video2World Workflow
1. Workflow File
2. Manual Model Installation
3. Complete Workflow  Step by Step
ComfyUI home page

Resources

installation
Tutorials
Development

Products

Features
Gallery
Download

Company

About
Careers
Terms of Service
Privacy Policy
github
x
discord
youtube
Powered by Mintlify