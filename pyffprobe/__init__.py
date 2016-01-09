import subprocess
import re
import os

class FfProbe:
    def __init__(self, media):
        self._media = media
        try:
            os.stat(self._media)
        except FileNotFoundError:
            raise FileNotFoundError("Media path not found.")
        # never forget that ffmpeg/ffprobe output to stderr
        self._ffprobe = str(subprocess.check_output(["ffprobe", self._media], stderr=subprocess.STDOUT))

    def get_ffprobe(self):
        return self._ffprobe

    def get_video_length(self):
        inputs = re.search("(Input.*)(Stream #0:0)", self._ffprobe)
        duration = re.search("(Duration: )(.*)(, s)", inputs.group(1))
        video_duration = duration.group(2)
        #return as string HH:MM:SS.mm
        return video_duration
