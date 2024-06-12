import numpy as np
import cv2

file_name = "C:\\Users\\P.Andishe\\Desktop\\New folder (5)\\uni.jpg"

## لود کردن تصویر
image = cv2.imread(f'{file_name}', cv2.IMREAD_GRAYSCALE)
image_array = np.array(image)

## تابع کانوولوشن دو بعدی
def main(image, filter_kernel):
    filter_height, filter_width = filter_kernel.shape
    image_height, image_width = image.shape
    
    conv_result = np.zeros((image_height, image_width))
    
    padded_image = np.pad(image, ((filter_height // 2, filter_height // 2), 
                                  (filter_width // 2, filter_width // 2)), mode='constant')
    
    for i in range(image_height):
        for j in range(image_width):
            region = padded_image[i:i + filter_height, j:j + filter_width]
            conv_result[i, j] = np.sum(region * filter_kernel)
    
    return conv_result

## تعریف فیلتر سوبل
sobel_x = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]])

sobel_y = np.array([[-1, -2, -1],
                    [ 0,  0,  0],
                    [ 1,  2,  1]])

## اجرای تابع کانوولوشن روی راستای ایکس و ایگرگ
edge_x = main(image_array, sobel_x)
edge_y = main(image_array, sobel_y)

edges = np.hypot(edge_x, edge_y)
edges = edges / edges.max() * 255

## نمایش و ذخیره فایل
cv2.imwrite(".\\res.png", edges.astype(np.uint8))
cv2.imshow('Edges', edges.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()
