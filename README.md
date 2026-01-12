# Signal Analysis and Audio Processing in Python 🎵📈

This repository contains a Python script focused on **time-domain and frequency-domain signal analysis**, applied to both synthetic signals and real audio data. The project makes use of the **Fast Fourier Transform (FFT)** and **ideal low-pass filtering** to study, filter, and reconstruct signals.

## Project Overview

The code is structured into three main sections:

---

## 1. Periodic Waveform Analysis (Section 7.1)

- Generation of:
  - Square wave
  - Sawtooth wave
- Computation of the FFT and its magnitude
- Application of an **ideal low-pass filter** using a rectangular window in the frequency domain
- Reconstruction of the filtered signals using the inverse FFT
- Graphical visualization of:
  - Time-domain signal
  - Frequency spectrum
  - Filtered spectrum
  - Reconstructed signal

---

## 2. Sinusoidal Signal Generation (Section 7.2)

- Generation of a **440 Hz sinusoidal signal (A4 tuning fork)**
- Sampling frequency: **44.1 kHz**
- Duration: **3 seconds**
- Optional export of the signal as a `.wav` audio file

---

## 3. Real Audio Signal Processing (Section 7.3)

- Reading an audio file (`piano-la3.wav`)
- Spectral analysis of a piano sound
- Low-pass filtering centered around **440 Hz**
- Reconstruction of the filtered signal using the inverse FFT
- Visualization in both time and frequency domains
- Optional normalization and export of the filtered audio

---

## Requirements

To run this project, you will need the following Python libraries:

- `numpy`
- `matplotlib`
- `scipy`

You can install them using:

```bash
pip install numpy matplotlib scipy
```

---

## Usage

To run this project, follow these steps:

1. Clone the repository to your local machine.
2. Make sure the audio file `piano-la3.wav` is located in the same directory as the Python script.
3. Run the script using Python:
   ```bash
   python main.py
   ```
4. The script will generate multiple figures showing:
    -Time-domain signals
    -Frequency spectra
    -Filtered spectra
    -Reconstructed signals
   
Several plotting windows will appear during execution displaying the results of each processing stage.

---

## Notes

- Lines related to audio file export using wavfile.write are commented out by default.
  They can be enabled if you wish to save the generated or filtered signals as .wav files.

- This project is intended for educational purposes, mainly to illustrate Fourier analysis,
  spectral filtering, and signal reconstruction concepts.
  
- Ensure that all required Python libraries are properly installed before running the script.

---

## License

This project is provided for academic and educational use.
You are free to modify, reuse, and extend the code for learning or research purposes.
