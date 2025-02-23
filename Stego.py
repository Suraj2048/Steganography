import cv2
import os

def encrypt_image(image_path, output_path, message):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found!")
        return False

    rows, cols, channels = img.shape
    total_pixels = rows * cols

    if len(message) > total_pixels:
        print("Error: Message too long to hide in the given image.")
        return False

    idx = 0
    # Embed message in the blue channel (channel index 0) sequentially
    for i in range(rows):
        for j in range(cols):
            if idx < len(message):
                # Save ASCII value of character into blue channel
                img[i, j, 0] = ord(message[idx])
                idx += 1
            else:
                break
        if idx >= len(message):
            break

    cv2.imwrite(output_path, img)
    os.system(f"start {output_path}")  # For Windows; adjust for other OS if needed
    return True

def decrypt_image(image_path, message_length):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found!")
        return None

    rows, cols, channels = img.shape
    message = ""
    idx = 0

    for i in range(rows):
        for j in range(cols):
            if idx < message_length:
                # Retrieve the ASCII value from the blue channel and convert it back to a character
                message += chr(img[i, j, 0])
                idx += 1
            else:
                break
        if idx >= message_length:
            break

    return message

def main():
    image_path = "test.jpg"
    output_path = "encryptedImage.png"  # Changed to PNG for lossless saving

    message = input("Enter secret message: ")
    password = input("Enter a passcode: ")

    # Encrypt the message into the image
    if encrypt_image(image_path, output_path, message):
        # Decryption process: ask for the passcode again
        input_password = input("Enter passcode for Decryption: ")
        if password == input_password:
            decrypted_message = decrypt_image(output_path, len(message))
            if decrypted_message is not None:
                print("Decrypted message:", decrypted_message)
        else:
            print("Invalid password! Access denied.")

if __name__ == "__main__":
    main()
