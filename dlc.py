import deeplabcut
import os
from os import listdir

def setupProject(projectName, videos):
    return deeplabcut.create_new_project(projectName, 'joshua', videos) 
    
def extract_frames(path_config):
    deeplabcut.extract_frames(path_config, 'automatic', 'kmeans')

def label_frames(path_config):
    deeplabcut.label_frames(path_config)

def getVideos(view, path):
    ### View can be 'side' or 'top'
    # video_path = os.path.expanduser('~/Documents/fyp_videos/Angle Robustness/')
    videos = listdir(path)
    videos = [path + video for video in videos if view in video]
    return videos

if __name__ == '__main__':
    setup = False
    video_path = os.path.expanduser('~/Documents/fyp_videos/Angle Robustness/')
    view = 'side'
    videos = getVideos(view, video_path)
    projectName = 'angle-robustness-' + view
    if setup:
        path = setupProject(projectName, videos)
        print(path)
    else:
        path = '/Users/joshuaramkissoon/Documents/fyp_videos/angle-robustness-side-joshua-2020-05-16/config.yaml'
        extract_frames(path)
        label_frames(path)







