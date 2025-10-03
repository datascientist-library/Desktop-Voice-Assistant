# Desktop Voice Assistant using Python

This project involves the creation of a desktop voice assistant using Python that can recognize voice commands, process them, and execute the required actions. The assistant can interact with different applications and services, such as Wikipedia, web browsers, and more.

---

## Project Overview

The voice assistant follows a multi-layer approach to recognize and interpret voice commands:

### 1) **Speech to Text**
   - Converts audio input into text that the assistant can process.

### 2) **Text Analysis**
   - Converts the text to something understandable by the computer, analyzing the command and mapping it to specific functions or parameters.

### 3) **Interpret Commands**
   - The computer interprets the command, communicates with the server, and executes the corresponding action.

---

## Libraries Used

### 1) **pyttsx3**
   - **Description:** A text-to-speech conversion library in Python. Works offline and is compatible with both Python 2 and 3. 
   - **Feature:** Converts the entered text into speech with two available voices (male and female) using the `SAPI5` engine on Windows.

### 2) **speechRecognition**
   - **Description:** An interdisciplinary field focused on developing technologies to enable computers to recognize and translate spoken language into text.

### 3) **datetime**
   - **Description:** A Python module used for manipulating dates and times. It helps in time-related functionalities like getting the current time, date, and calculating time differences.

### 4) **Wikipedia**
   - **Description:** A Python library that interacts with the Wikipedia API. Allows you to search for articles, get summaries, links, and images from Wikipedia pages.

### 5) **webbrowser**
   - **Description:** A Python module that provides an interface for opening and displaying web documents in a browser across multiple platforms.

### 6) **os**
   - **Description:** A Python module used to interact with the operating system, enabling interaction with the file system and other OS-level functionalities.

---

## Data Preprocessing

- **Audio Data Loading:** 
   - Reads the audio data from a file and loads it into a 2D NumPy array.
   - This array contains a sequence of numbers, each representing a measurement of sound intensity or amplitude.

- **Conversion to Uniform Dimensions:** 
   - Standardizes the audio data into consistent dimensions like sample rate, channels, and duration.

- **Data Augmentation:**
   - Adds more variety to the audio input to help the model generalize better to different types of inputs.

- **Mel Spectrograms:** 
   - Converts the raw audio data into Mel Spectrograms, which visually represent the audio in terms of frequency content.

---

## Architecture

The core architecture of the voice assistant combines **Convolutional Neural Networks (CNNs)** with **Recurrent Neural Networks (RNNs)** for processing the speech data.

### CNN + RNN-based Architecture:
- The CNN layers process the Mel Spectrogram images and output feature maps.
- Bidirectional LSTM layers process the feature maps as a sequence of timesteps to recognize the characters corresponding to the speech.
- Softmax layer produces character probabilities, and the model uses CTC (Connectionist Temporal Classification) Loss to align speech with text.

### Bidirectional LSTM & Softmax:
- Bidirectional LSTM layers learn from both past and future timesteps, improving the understanding of the speech context.
- Softmax activation at the end of the network helps convert the learned features into readable text predictions.

---

## Advantages

- **Smart and Compact Devices:** 
   - These applications can help create compact, multi-functional devices capable of handling several tasks.
   
- **Data Import/Export:** 
   - Facilitates seamless data transfers and retrievals from various services.

- **Task Automation:** 
   - The assistant can help control applications, schedule reminders, and manage tasks based on commands.

- **Location-Based Services:** 
   - The voice assistant can offer location-based information and services for a more personalized experience.

- **Day Planning & Reminders:** 
   - The assistant helps you plan your day, set reminders, and notify you of important events at the right time and place.
