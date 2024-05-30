from utils import read_video,save_video
from trackers import Tracker
def main():
  # read video
  video_frames = read_video('videos/08fd33_4.mp4')

  # initialize tracker
  tracker = Tracker('models/best.pt')

  tracker.get_object_tracks(video_frames)

  # save video
  save_video(video_frames,'output_videos/output.avi')

if __name__ == '__main__':
  main()