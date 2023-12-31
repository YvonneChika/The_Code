# import torch
# import torchvision.transforms as transforms
# from PIL import Image

# def quantify_change(image_path1, image_path2):
#     model = torch.hub.load('pytorch/vision:v0.11.1', 'deeplabv3_resnet101', pretrained=True)
#     model.eval()

#     # Load and preprocess the images
#     transform = transforms.Compose([
#         transforms.ToTensor(),
#         transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
#     ])
#     image1 = transform(Image.open(image_path1).convert("RGB"))
#     image2 = transform(Image.open(image_path2).convert("RGB"))

#     # Expand dimensions to match the model input shape
#     image1 = image1.unsqueeze(0)
#     image2 = image2.unsqueeze(0)

#     # Obtain the output segmentation maps
#     with torch.no_grad():
#         output1 = model(image1)['out']
#         output2 = model(image2)['out']

#     # Calculate the change score
#     change_score = torch.mean(torch.abs(output1 - output2))

#     # Normalize the change score between 0 and 1
#     change_score_normalized = 1 - (change_score / 2.0)

#     return change_score_normalized.item()

# # Example usage
# image_path1 = 'pcd/set0/train/t0/00000091.jpg'
# image_path2 = 'pcd/set0/train/t1/00000091.jpg'

# change_score = quantify_change(image_path1, image_path2)
# print(f"Normalized Change Score: {change_score}")
import torch
import torchvision.transforms as transforms
from PIL import Image

def calculate_matching_percentage(image1, image2):
    matching_pixels = torch.sum(image1 == image2).item()
    total_pixels = image1.numel()
    matching_percentage = (matching_pixels / total_pixels) * 100
    return matching_percentage

def detect_matching_percentage(image_path1, image_path2):
    # Load and preprocess the images as tensors
    transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.ToTensor(),
    ])
    image1 = transform(Image.open(image_path1).convert("RGB"))
    image2 = transform(Image.open(image_path2).convert("RGB"))

    # Calculate the percentage of matching tensor values
    matching_percentage = calculate_matching_percentage(image1, image2)

    return matching_percentage



image_path1 = 'pcd/set0/train/t0/00000038.jpg'
image_path2 = 'pcd/set0/train/t1/00000038.jpg'


matching_percentage = detect_matching_percentage(image_path1, image_path2)
print(f"Matching Percentage: {matching_percentage:.2f}%")