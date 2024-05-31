from utils import read_video,save_video
from trackers import Tracker
def main():
  # read video
  video_frames = read_video('Analysis-System/videos/08fd33_4.mp4')

  # initialize tracker
  tracker = Tracker('Analysis-System/models/best.pt')

  tracks = tracker.get_object_tracks(video_frames,
                            read_from_stub=True,
                            stub_path='Analysis-System/stubs/track_stubs.pk1')
  
  # draw output
  ## draw object tracks
  output_video_frames = tracker.draw_annotations(video_frames,tracks)

  # save video
  save_video(output_video_frames,'Analysis-System/output_videos/output_video.avi')

if __name__ == '__main__':
  main()

  