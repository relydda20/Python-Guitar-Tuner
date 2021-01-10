from tkinter import *
import pyaudio
import numpy as np
import os 
import threading

#Frequency of each note in Hz
E2_freq = 164.81  
A2_freq = 220.00
D3_freq = 146.83
G3_freq = 196.00
B3_freq = 246.23
E4_freq = 329.23

maxFreq = 330

Sample_Rate = 44100     # Sampling frequency in Hz
Chunk = 21050            # The number of frames in the buffer
Samples_Per_Buffer = 44100 #Used determine how much data that can be processed 

# Creating a zero array to be used as a buffer when receiving input
buffer = np.zeros(Samples_Per_Buffer, dtype=np.float32)

# Defining the audio stream and starting it
stream = pyaudio.PyAudio().open(format=pyaudio.paFloat32,
                                channels=1,
                                rate=Sample_Rate,
                                input=True,
                                frames_per_buffer=Chunk)

stream.start_stream()

# A function for the input to be processed to find the max frequency of a buffer
def start_stream():
  while stream.is_active:
    buffer[-Chunk:] = np.frombuffer(stream.read(Chunk), np.int32) # Appending new buffers by clearing out the old one

    FFT = np.fft.fft(buffer) # Using the FFT algorithm to process the DFT

    Freq = np.abs(FFT[:maxFreq]).argmax() # Finding the maximum frequency
      
    print("The guitar frequency is {:.2f} Hz".format(Freq))

# Threading Process to run the GUI and the audio processing simultaneously
Thread = threading.Thread(target=start_stream, daemon = True)
Thread.start()

# The GUI for each of the Notes
class TunerGUI:
  def __init__(self, master,):
    self.__master = master
    self.__master.title("Python Guitar Tuner")
    self.__master.geometry = ("600 x 600")    

    self.__label = Label(master, text="Click the Note you want to tune your guitar to!")
    self.__label.pack()

    self.__e2_button = Button(master, text = "E2", command=tune_to_E2)
    self.__e2_button.pack()

    self.__a2_button = Button(master, text = "A2", command=tune_to_A2)
    self.__a2_button.pack()
    
    self.__d3_button = Button(master, text = "D3", command=tune_to_D3)
    self.__d3_button.pack()

    self.__G3_button = Button(master, text = "G2", command=tune_to_G3)
    self.__G3_button.pack()          

    self.__B3_button = Button(master, text = "B3", command=tune_to_B3)
    self.__B3_button.pack()

    self.__E4_button = Button(master, text = "E4", command=tune_to_E4)
    self.__E4_button.pack()

    self.__E2_label = Label(master, text = "E2 = 164.81 Hz")
    self.__E2_label.pack()

    self.__E2_label = Label(master, text = "A2 = 220.00 Hz")
    self.__E2_label.pack()                         

    self.__E2_label = Label(master, text = "D3 = 146.83 Hz")
    self.__E2_label.pack()       

    self.__E2_label = Label(master, text = "G3 = 196.00 Hz")
    self.__E2_label.pack()       

    self.__E2_label = Label(master, text = "B3 = 246.23 Hz")
    self.__E2_label.pack()       

    self.__E2_label = Label(master, text = "E4 = 329.23 Hz")
    self.__E2_label.pack()       

    self.close_button = Button(master, text="Close", command=master.quit)
    self.close_button.pack()

# Function to check if the user is tuned to E2
def tune_to_E2():
  FFT = np.fft.fft(buffer) # Using the FFT algorithm to process the DFT

  Freq = (np.abs(FFT[:maxFreq]).argmax()) # Finding the maximum frequency

  if ( Freq < E2_freq):
    os.system('cls' if os.name=='nt' else 'clear')
    difference = E2_freq - Freq
    print("Tune {:2f} Hz Higher".format(difference))
  if (Freq > E2_freq):
    os.system('cls' if os.name=='nt' else 'clear')
    difference = Freq - E2_freq
    print("Tune {:2f} Hz Lower".format(difference))

# Function to check if the user is tuned to A2
def tune_to_A2():
  FFT = np.fft.fft(buffer) # Using the FFT algorithm to process the DFT

  Freq = (np.abs(FFT[:maxFreq]).argmax()) # Finding the maximum frequency

  if ( Freq < A2_freq):
    os.system('cls' if os.name=='nt' else 'clear')
    difference = A2_freq - Freq
    print("Tune {:2f} Hz Higher".format(difference))
  if (Freq > A2_freq):
    os.system('cls' if os.name=='nt' else 'clear')
    difference = Freq - A2_freq
    print("Tune {:2f} Hz Lower".format(difference))

# Function to check if the user is tuned to D3
def tune_to_D3():
  FFT = np.fft.fft(buffer) # Using the FFT algorithm to process the DFT

  Freq = (np.abs(FFT[:maxFreq]).argmax()) # Finding the maximum frequency

  if ( Freq < D3_freq):
    os.system('cls' if os.name=='nt' else 'clear')
    difference = D3_freq - Freq
    print("Tune {:2f} Hz Higher".format(difference))
  if (Freq > D3_freq):
    os.system('cls' if os.name=='nt' else 'clear')
    difference = Freq - D3_freq
    print("Tune {:2f} Hz Lower".format(difference))

# Function to check if the user is tuned to G3
def tune_to_G3(): 
  FFT = np.fft.fft(buffer) # Using the FFT algorithm to process the DFT

  Freq = (np.abs(FFT[:maxFreq]).argmax()) # Finding the maximum frequency
     
  if ( Freq < G3_freq):
    os.system('cls' if os.name=='nt' else 'clear')
    difference = G3_freq - Freq
    print("Tune {:2f} Hz Higher".format(difference))
  if (Freq > G3_freq):
    os.system('cls' if os.name=='nt' else 'clear')
    difference = Freq - G3_freq
    print("Tune {:2f} Hz Lower".format(difference))

# Function to check if the user is tuned to B3
def tune_to_B3():
  FFT = np.fft.fft(buffer) # Using the FFT algorithm to process the DFT

  Freq = (np.abs(FFT[:maxFreq]).argmax()) # Finding the maximum frequency
     
  if ( Freq < B3_freq):
    os.system('cls' if os.name=='nt' else 'clear')
    difference = B3_freq - Freq
    print("Tune {:2f} Hz Higher".format(difference))
  if (Freq > B3_freq):
    os.system('cls' if os.name=='nt' else 'clear')
    difference = Freq - B3_freq
    print("Tune {:2f} Hz Lower".format(difference))

# Function to check if the user is tuned to E4
def tune_to_E4():
  FFT = np.fft.fft(buffer) # Using the FFT algorithm to process the DFT

  Freq = (np.abs(FFT[:maxFreq]).argmax()) # Finding the maximum frequency
    
  if ( Freq < E4_freq):
    os.system('cls' if os.name=='nt' else 'clear')
    difference = E4_freq - Freq
    print("Tune {:2f} Hz Higher".format(difference))
  if (Freq > E4_freq):
    os.system('cls' if os.name=='nt' else 'clear')
    difference = Freq - E4_freq
    print("Tune {:2f} Hz Lower".format(difference))
    
root = Tk()
my_gui = TunerGUI(root)
root.mainloop()