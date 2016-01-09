from nose.tools import *
import pyffprobe

def setup():
    pass

def teardown():
    pass

def test_class_init():
    p = pyffprobe.FfProbe("/media/alexander/New Volume/vgvideo/2016-01-08 23-02-55.mp4")

@raises(FileNotFoundError)
def test_class_init_no_file():
    p = pyffprobe.FfProbe("nonsense")

def test_get_ffprobe():
    p = pyffprobe.FfProbe("/media/alexander/New Volume/vgvideo/2016-01-08 23-02-55.mp4")
    p3 = p.get_ffprobe()
    assert_true(len(p3) is not 0)
