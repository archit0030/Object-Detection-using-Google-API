import google.generativeai as genai
from IPython.display import display
import PIL.Image
import PIL.ImageDraw

# Configure the API key
genai.configure(api_key="YOUR_API_KEY")

# Choose a Gemini API model.
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")

# Open the image file
sample_file_2 = PIL.Image.open('OIP (2).jpeg')

# Define the prompt
prompt = "Return a bounding box for the mop basket . \n [ymin, xmin, ymax, xmax]"

# Generate the bounding box coordinates
response = model.generate_content([sample_file_2, prompt])

# Print the raw response for debugging
print("Raw API response:", response.text)

# Extract the bounding box coordinates from the response

bbox = eval(response.text.strip())
print("Extracted bounding box coordinates:", bbox)

# Ensure the bounding box coordinates are correct
if len(bbox) == 4:
    ymin, xmin, ymax, xmax = bbox

    # Get image dimensions
    width, height = sample_file_2.size
    print(f"Image dimensions: width={width}, height={height}")

    # Assuming the coordinates from the response are in a different scale
    # Scale the coordinates to match the image size
    ymin = ymin * height / 1000
    ymax = ymax * height / 1000
    xmin = xmin * width / 1000
    xmax = xmax * width / 1000

    # Print the scaled coordinates
    print(f"Scaled bounding box coordinates: {[ymin, xmin, ymax, xmax]}")

    # Ensure coordinates are within image bounds
    if 0 <= xmin < width and 0 <= xmax < width and 0 <= ymin < height and 0 <= ymax < height:
        # Draw the bounding box on the image
        draw = PIL.ImageDraw.Draw(sample_file_2)
        draw.rectangle([xmin, ymin, xmax, ymax], outline="red", width=3)

        # Display the image with the bounding box
        display(sample_file_2)
    else:
        print("Scaled bounding box coordinates are out of image bounds:", [ymin, xmin, ymax, xmax])
else:
    print("Invalid bounding box coordinates received:", bbox)

