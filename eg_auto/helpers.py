import os
import time

import numpy as np
import scipy
from scipy.ndimage import label

import PIL
from PIL import Image

import skimage
import skimage.io as sio

import matplotlib
import matplotlib.animation
import matplotlib.pyplot as plt

def check_connected(body):

    # check if body plan (np.array) is connected
    #

    labels = label(body)[0]

    if labels.max() > 1:
        return False
    else:
        return True

def make_gif(frames_path="./frames/", gif_path="./assets", \
        tag="no_tag", speedup=3, scale=1.0):
    
    dir_list = os.listdir(frames_path)

    frames = []

    dir_list.sort()
    for ii, filename in enumerate(dir_list):
   
        if "png" in filename and (ii % speedup) == 0:

            image_path = os.path.join(frames_path, filename)
            frames.append(Image.open(image_path))

    assert len(frames) > 1, "no frames to make gif"

    first_frame = frames[0]
    
    gif_id = int((time.time() % 1)*1000)

    gif_path = os.path.join(gif_path, f"gif_{tag}_{gif_id:04d}_{speedup}X.gif") 

    first_frame.save(gif_path, format="GIF", append_images=frames, \
            save_all=True, duration=42, loop=0)

    rm_path = os.path.join(frames_path, "*png")

    os.system(f"rm {rm_path}")

def make_fig(frame):
    global plot_0
    global ax
    global frames

    fig, ax = plt.subplots(1,1, figsize=(12,8), facecolor="white")


    plot_0 = ax.imshow(frame, interpolation="nearest")

    ax.set_yticklabels("")
    ax.set_xticklabels("")

    plt.tight_layout()

    return fig, ax

def update_fig(ii):
    global plot_0
    global ax
    global frames

    plot_0.set_array(frames[ii+1])


def make_mp4(frames_path="./frames/", mp4_path="./assets", \
        tag="no_tag", speedup=1, scale=1.0):

    dir_list = os.listdir(frames_path)

    global frames

    frames = []

    dir_list.sort()

    for ii, filename in enumerate(dir_list):
   
        if "png" in filename and (ii % speedup) == 0:

            image_path = os.path.join(frames_path, filename)
            frames.append(sio.imread(image_path))

    assert len(frames) > 1, "no frames to make gif"

    first_frame = frames[0]
    
    mp4_id = int((time.time() % 1)*1000)

    mp4_path = os.path.join(mp4_path, f"{tag}_{mp4_id:04d}_{speedup}X.mp4") 

    fig, ax = make_fig(first_frame)
    num_frames = len(frames) - 1

    msg = f"saving to {mp4_path}"
    print(msg)

    t0 = time.time()
    matplotlib.animation.FuncAnimation(fig, update_fig, frames=num_frames, interval=10).save(mp4_path)
    t1 = time.time()
    msg = f"it took {t1-t0:.3f} seconds to save the animation"
    print(msg)

    rm_path = os.path.join(frames_path, "*png")

    os.system(f"rm {rm_path}")

