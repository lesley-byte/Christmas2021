# Christmas 2021 Keyboard
If you know, then you know. 🎄

Your kit should include:
1. "Merry Christmas here's a keyboard" green pcb. (See images below)
2. Buttons that may or may not be attached
3. A brand new unused Raspberry Pi pico
4. A small usb cable

![image](https://user-images.githubusercontent.com/60296103/145315846-69aa06cc-9ada-4acf-b107-ad9da7a73005.png)
![image](https://user-images.githubusercontent.com/60296103/145315960-891df17c-c62c-4927-922e-38e7cc167c39.png)


# *Start*


The Raspberry Pi Pico *needs* firmware.  I gave you a fresh one. This is an adventure. *Buckle up!* The example code here uses CircuitPython but if you want to you can use something else.
its up to you.

1. Familiarize yourself with the Pico.  There's a great introduction on the adafruit website at: https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython  ![image](https://user-images.githubusercontent.com/60296103/145462037-aeacaa23-bd2e-4a99-81da-0be189f1a5a9.png)

2. Follow the instructions for setting up the Pico macropad here: https://learn.adafruit.com/diy-pico-mechanical-keyboard-with-fritzing-circuitpython/overview 
![image](https://user-images.githubusercontent.com/60296103/145460446-f6251766-12cc-4575-ab9b-556eb37764c9.png)

but stop at the code page.  And don't worry about 3d printing.  We aren't doing that right now...(I haven't created the files for that kind of thing)or if you don't stop at the code, just realize that you will have to alter it to work in this situation.  The attached usb cable can be used.  If you want to use your own cable, thats fine, just make sure it is a data cable and not just a charging cable.
- Download the latest version of circuitpython for the pico https://circuitpython.org/board/raspberry_pi_pico/ 
 ![image](https://user-images.githubusercontent.com/60296103/145460202-6ccdd925-580b-49af-8095-1d56f8d3c44c.png)

- Follow the instructions to put the circuitpython on the pico https://learn.adafruit.com/diy-pico-mechanical-keyboard-with-fritzing-circuitpython/installing-circuitpython
![image](https://user-images.githubusercontent.com/60296103/145462220-161ac3ea-4a11-4bcf-b91a-a6aa01a13daa.png)


- Download the Adafruit Hid library https://circuitpython.org/libraries  (you want the Bundle for Version 7.x)
![image](https://user-images.githubusercontent.com/60296103/145462373-19e73bf8-e885-41ed-8cf6-77676866c4bb.png)


- Install Mu or use python IDE of your choice to your computer.  https://codewith.mu/
![image](https://user-images.githubusercontent.com/60296103/145462879-61b292b5-6fe5-4dc0-83e8-bd16f9c59245.png)


4. Go to the page in this repository for the code.  You can cut and paste it into the editor or you can mess with it and change it as you see fit.  Its yours.  
    https://github.com/lesley-byte/Christmas2021/blob/a56719320f9c8117c5a0f90006cdf598d7aba63f/code.py
    - Copy the code.py file and paste it into Mu or your editor of choice. Then, save it to your Pico as code.py.
    
    ### *Note:* The code must be saved in a file called:  code.py
    
5. Keyboard assembly:
  - Make sure your code is saved.
  - Eject/detach Pico from your computer.
  - Plug Pico into Christmas keyboard.
  - Plug assembled Christmas keyboard into  your computer.  It will pop up as a usb drive.  There is a way around this with code if it becomes annoying.  Its just easier to change the code if it acts like a usb drive.  Close the popped up folder and use it like a keyboard, macropad, whatever you want.

 6. Play!!

# Ask me if you need help.  

I will actually set it up for you if you want but am offering it as an adventure first.  This way you can learn to do this with any pico... and even on a breadboard with different button layouts.
