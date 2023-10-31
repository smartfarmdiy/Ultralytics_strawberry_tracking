# Ultralytics_strawberry_tracking
Hello everyone welcome to my repository. I will show you how to use Ultralytics for Multiple objects tracking(MOT).
enjoy !!!

## Preparation stage
You need to have in tracking objects are as follows

**1. Visual Studio Code** (Download and Install from [VSCODE](https://code.visualstudio.com/))

**2. Package and Library**
   - Python>=3.9 (Download and Install from [Python](https://www.python.org/downloads/))
   - [Opencv](https://opencv.org/) (use command prompt)
           <pre> pip install opencv-contrib-python </pre>
   - [Pytorch](https://pytorch.org/)
   - [Ultralytics](https://www.ultralytics.com/)(use command prompt)
           <pre> pip install ultralytics </pre>
   - Nvidia GPU Computing Toolkit ([cudav11.7](https://developer.nvidia.com/cuda-11-7-0-download-archive), [cudnn](https://developer.nvidia.com/cudnn))
     Windows10 --> x86_64 --> exe (local) --> run .exe file for install
     
     ![image](https://github.com/smartfarmdiy/Ultralytics_strawberry_tracking/assets/63504401/b7538474-f88b-47cd-b729-d170c098be4e)

     ![image](https://github.com/smartfarmdiy/Ultralytics_strawberry_tracking/assets/63504401/728854b7-4f0e-4052-8abd-b5d0755cf258)

      Extract .zip file then move the files in these folders to CUDA.
              <pre>
                    bin ==> C:/Programe files/Nvidia GPU Computing Toolkit/CUDA/v11.7/bin
                    lib ==> C:/Programe files/Nvidia GPU Computing Toolkit/CUDA/v11.7/lib
                    include ==> C:/Programe files/Nvidia GPU Computing Toolkit/CUDA/v11.7/include
              </pre>


   ## Coding stage
   **1. Import Custom Model** I have a model for you. It is in the "Custom Model" folder
   
   ![image](https://github.com/smartfarmdiy/Ultralytics_strawberry_tracking/assets/63504401/23af9133-22e8-4b88-bc73-c88cfcbbf0f7)

   **2. Use Model for Tracking** It is an implementation of the model for multi-object tracking. With the Ultralytics tracker, follow these steps:

   - Import needed packages
     <pre> 
      import cv2
      from ultralytics import YOLO
      import torch
      </pre>
   - Import Custom Model and Used GPU
     <pre>
      model_path = 'include model path'
      model = YOLO(model_path).to(torch.device(0))
     </pre>
   - Open Usb Camera (0 is port of usb camera)
     <pre>
      cap = cv2.VideoCapTure(0)
     </pre>
   - 123
   - 123
   - 123

