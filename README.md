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
   - Use Ultralytics Tracking
     <pre>
      results = model.track(source=frame, persist=True, iou=0.6, conf=0.4)
     </pre>
     You can get data (bounging boxes, object_ids, cofidence, class_ids)
     <pre>
         track_data = results[0].boxes.data.int().cuda().tolist()
     </pre>
     or (bounging boxes)
     <pre>
        track_xyxy = results[0].boxes.xyxy.int().cuda().tolist()
     </pre>
     or (object_ids)
     <pre>
        track_ids = results[0].boxes.id.int().cuda().tolist()
     </pre>
   - Show output on display
     <pre>
        annotated_frame = results[0].plot()
        cv2.imshow("Output Tracking", annotated_frame)
        if cv2.waiKey(1) & 0xFF == ord("e"):
           break
     </pre>

   ## Safety precautions
   
   **1. Follow the Nvidia Jetson Nano instruction manual.**
   
   **2. Avoid exposing the device to static electricity.**
   
   **3. Should install Package and Library versions that are compatible to reduce error_version problems.**
   
   **4. Administrator rights should be used to perform various actions to reduce permission_error problems.**
   

