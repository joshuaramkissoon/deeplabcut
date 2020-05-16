import deeplabcut
import os
from os import listdir







def setup(projectName, videos):
    path_config = deeplabcut.create_new_project(projectName, 'joshua', videos) 
    print(path_config)
    # extract_frames(path_config)
    # label_frames(path_config)
    
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
    video_path = os.path.expanduser('~/Documents/fyp_videos/Angle Robustness/')
    view = 'side'
    videos = getVideos(view, video_path)
    projectName = 'angle-robustness-' + view
    # setup(projectName, videos)
    path = '/Users/joshuaramkissoon/Documents/fyp_videos/angle-robustness-top-joshua-2020-05-15/config.yaml'
    # extract_frames(path)
    label_frames(path)







