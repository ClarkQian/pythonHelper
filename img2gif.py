# img -> gif

import os
import imageio
 
def create_gif(image_list, gif_name):
 
    frames = []
    for image_name in image_list:
        if image_name.endswith('.jpg'):
            print(image_name)
            frames.append(imageio.imread(image_name))
    # Save them as frames into a gif
    imageio.mimsave(gif_name, frames, 'GIF', duration = 0.1)
 
    return
 
def main():
 
    path=r'./img_output/transfer_12_43/'
    image_list=[ path+img for img in  os.listdir(path)]
#     print(image_list)
    gif_name = './img_output/transfer_12_43/created_gif.gif'
    create_gif(image_list, gif_name)
 
if __name__ == "__main__":
    main()
