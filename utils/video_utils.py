import cv2

def read_video(video_path):
  cap = cv2.VideoCapture(video_path)
  frames = []
  while True:
    ret,frame = cap.read()
    if not ret:
      break
    # adds frame by frame to the list
    frames.append(frame)
  return frames

def save_video(output_video_frames,output_video_path):
  fourcc = cv2.VideoWriter_fourcc(*'XVID') #define output format xvid
  out = cv2.VideoWriter(output_video_path,fourcc,24,(output_video_frames[0].shape[1],output_video_frames[0].shape[0])) # 24 is fps, then width and height of the frame
  for frame in output_video_frames:
    out.write(frame)
  out.release()