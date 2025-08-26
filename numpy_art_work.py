import numpy as np
from PIL import Image

def numpy_art_studio(image_path):
    """
    Welcome to the NumPy Art Studio! 🎨
    
    This program takes a digital image and transforms it using the power of NumPy.
    Think of an image not just as a picture, but as a grid of numbers—a NumPy array.
    Each number represents a pixel's color and brightness. By manipulating this grid
    of numbers, we can create stunning visual effects!
    """
    print("✨ Welcome to the NumPy Art Studio! ✨")
    print("We're about to turn a picture into a grid of numbers and then play with them.")
    print("-" * 50)
    
    try:
        # Step 1: Laying the Foundation - From Picture to Numbers
        # We start by opening the image and turning it into a multi-dimensional NumPy array.
        # This array is our canvas. For a color image, it's a 3D grid:
        # (height, width, color_channels).
        print(f"Loading '{image_path}'...")
        the_picture = Image.open(image_path)
        our_canvas = np.array(the_picture)
        
        # Let's see what we're working with.
        print(f"The picture is now a NumPy array with a shape of {our_canvas.shape}.")
        print(f"Its pixel values are stored as {our_canvas.dtype} numbers (0-255).")
        print("-" * 50)

        # Step 2: The Brightness Brush - A Lesson in Broadcasting
        # Imagine wanting to make every single pixel brighter. You don't have to visit
        # each one individually! NumPy's "broadcasting" lets us add a single value
        # to every element in the array all at once. It's incredibly fast and efficient.
        print("Applying a brightness filter using NumPy's broadcasting magic...")
        brightness_boost = 75
        # We add a constant value to every pixel. np.clip makes sure no values
        # go beyond the 0-255 range, like a guardrail on a highway.
        brighter_canvas = np.clip(our_canvas + brightness_boost, 0, 255).astype(np.uint8)
        
        # Now, let's save our masterpiece.
        brighter_picture = Image.fromarray(brighter_canvas)
        brighter_picture.save("brighter_day.jpg")
        print(f"✓ Created 'brighter_day.jpg'. A simple brush stroke, applied everywhere!")
        print("-" * 50)
        
        # Step 3: Color Wizardry - Precision with Slicing
        # What if we only want to change the red tones in our picture? NumPy's "slicing"
        # lets us do just that. We can isolate a specific part of our grid, like
        # only the red color channel, and work on it exclusively.
        print("Now, let's boost the red tones using precise slicing...")
        # Create a copy so we don't mess up our original canvas.
        color_canvas = our_canvas.copy()
        
        # The syntax [:, :, 0] is our magical slice. It means:
        # [all rows, all columns, the first color channel (Red)]
        red_channel = color_canvas[:, :, 0]
        
        # We increase the value of every pixel in just the red channel.
        red_boost_value = 100
        red_channel_boosted = np.clip(red_channel + red_boost_value, 0, 255).astype(np.uint8)
        
        # Now, we put the boosted red channel back into our canvas.
        color_canvas[:, :, 0] = red_channel_boosted
        
        # And save this vibrant new version!
        red_boosted_picture = Image.fromarray(color_canvas)
        red_boosted_picture.save("crimson_sunset.jpg")
        print(f"✓ Created 'crimson_sunset.jpg'. A targeted splash of color!")
        print("-" * 50)
        
        print("Art session complete! Your transformed images are ready to be viewed. 🖼️")
        
    except FileNotFoundError:
        print(f"🚫 Error: Oops! It seems '{image_path}' isn't here. Please check the file path.")
    except Exception as e:
        print(f"🚫 An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Just place an image file (e.g., 'sunset.jpg') in the same folder as this script.
    image_file = "sunset.jpg" 
    numpy_art_studio(image_file)
