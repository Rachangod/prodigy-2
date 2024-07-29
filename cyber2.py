from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, shift):
    """
    Encrypts an image by shifting pixel values.
    
    :param input_path: Path to the input image
    :param output_path: Path to save the encrypted image
    :param shift: The value to add to each pixel
    """
    img = Image.open(input_path)
    pixels = np.array(img, dtype=np.uint8)  # Convert image to numpy array with uint8 dtype
    
    # Ensure shift value is positive and within a reasonable range
    shift = shift % 256
    
    # Encrypt pixel values by adding the shift value
    encrypted_pixels = (pixels + shift).astype(np.uint8)  # Ensure the result is uint8
    encrypted_img = Image.fromarray(encrypted_pixels)
    
    encrypted_img.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(input_path, output_path, shift):
    """
    Decrypts an image by reversing the pixel shift.
    
    :param input_path: Path to the encrypted image
    :param output_path: Path to save the decrypted image
    :param shift: The value to subtract from each pixel
    """
    img = Image.open(input_path)
    pixels = np.array(img, dtype=np.uint8)  # Convert image to numpy array with uint8 dtype
    
    # Ensure shift value is positive and within a reasonable range
    shift = shift % 256
    
    # Decrypt pixel values by subtracting the shift value
    decrypted_pixels = (pixels - shift).astype(np.uint8)  # Ensure the result is uint8
    decrypted_img = Image.fromarray(decrypted_pixels)
    
    decrypted_img.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

def main():
    print("Simple Image Encryption Tool")
    
    mode = input("Enter mode (encrypt/decrypt): ").strip().lower()
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")
        return

    input_path = input("Enter the path to the image file: ").strip()
    output_path = input("Enter the path to save the output image: ").strip()
    
    try:
        shift = int(input("Enter the shift value (integer): ").strip())
    except ValueError:
        print("Invalid shift value. Please enter an integer.")
        return
    
    if mode == 'encrypt':
        encrypt_image(input_path, output_path, shift)
    elif mode == 'decrypt':
        decrypt_image(input_path, output_path, shift)

if __name__ == "__main__":
    main()
