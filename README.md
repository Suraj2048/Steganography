# Steganography
Secure Data Hiding in Image Using Steganography 

**Image Steganography using OpenCV (JPG Format)**

📌**Project Overview**
This project implements image steganography, allowing users to hide and retrieve secret messages within an image by modifying pixel values. The hidden message is embedded in the blue channel of the image, and a password-protected decryption ensures only authorized users can access the data.

🔍**Features**
✅ Hide a text message inside a JPG image without visual distortion.
✅ Password-protected decryption for secure retrieval.
✅ Simple and lightweight, using only Python and OpenCV.
✅ Works on Windows, macOS, and Linux.

🛠**Technologies Used**
Programming Language: Python
Libraries: OpenCV (cv2), OS
Image Format: JPG (lossy format, may slightly alter pixel values)
Encoding Technique: Pixel value modification in the blue channe

📥**Installation & Setup**
1️⃣**Prerequisites**
Ensure you have Python 3.x installed. Then, install the required dependencies:
_pip install opencv-python_

2️⃣**Clone the Repository**

3️⃣**Run the Script**
_python Stego.py_

🚀**Usage**
1️⃣ Run the script and enter the secret message to hide inside an image.
2️⃣ Provide a passcode for securing the message.
3️⃣ The script will generate an encrypted image (encryptedImage.jpg) containing the hidden text.
4️⃣ To decrypt, enter the correct passcode and retrieve the original message.

🎯**End Users**
🔹 Cybersecurity enthusiasts – Learn about steganography techniques.
🔹 Individuals needing secure communication – Hide confidential messages inside images.
🔹 Digital watermarking applications – Protect digital assets with hidden data.
🔹 Data security professionals – Explore steganography for covert communication.

🏆 Wow Factor
✨ Embeds messages within JPG images, making them invisible to the human eye.
✨ Password-protected decryption ensures only authorized users can access the message.
✨ Lightweight and runs entirely offline, requiring no external servers.
✨ Works with any standard image viewer, as it does not visually alter the image.

🔗 GitHub Repository
