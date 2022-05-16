## Description
MystiQ is a GUI for [FFmpeg](http://ffmpeg.org), a powerful media converter.
FFmpeg can read audio and video files in various formats and convert them into
other formats. MystiQ features an intuitive graphical interface and a rich set
of presets to help you convert media files within a few clicks. Advanced users
can also adjust conversion parameters in detail.

## Instructions

This is a third-party Copr repository for MystiQ.
On Fedora and CentOS you will need to make use of the [RPMFusion](https://rpmfusion.org/Configuration) repository for ffmpeg.

This package should work on OpenSUSE as well (not tested)

Install with
```
sudo dnf copr enable jackgreiner/MystiQ
sudo dnf update --refresh
sudo dnf install mystiq
```
