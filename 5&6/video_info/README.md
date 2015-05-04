Scripts that perform the following functions

__Frame skipping__: Reducing the number of frames in the video by extracting one frame per second.
```
python preprocess.py --command shrink --source /path/to/input/file --dest /path/to/output/file
```


__Region of Interest (ROI) extraction__: Allows you to sepcify a rectangular ROI to extract from a video. Crops the video.
```
python preprocess.py --command roi --source /path/to/input/file --dest /path/to/output/file --rect x1,y1,x2,y2
```


__Scene Detection/Keyframe Selection__: Outputs a set of frames that represent transition points in the video. Will output the frames as well as a metadata file with data collected during the process. This data will include dominant colors in the images for the keyframes.

```
python scene_detection.py -s /path/to/input/file -d /path/to/output/folder -n identifierName -a excludeFramesBeforeThisIndex"
```
-n idenitifierName: This is a name useful to identify this video. It will be written into the metadata file for later cross referencing. Also a subfolder with this name will be generated in dest folder and that is where the data will go. Generated images will use this name as a prefix.

-a excludeBefore: An optional parameter. If you want to skip a certain number of frames at the beginning of the video from being considered, put the frame number here. In a video that has been frameskipped this will be equal to the seconds on the clock for when you want to start extracting frames.

This will generate an output folder with subfolders that contain images at various scales. The frame number is appended to the image name.



__Postprocessing__: A script to combine the metadata files from multiple videos into one.
```
python postprocess.py -s path/to/source/folder -d path/to/dest/folder
```

Will recursively look into source folder for metadata-keyframe.json files generated in the previous step. Will then concatenate them into one metadata.json file that will be placed in the output folder. Run this after processing all your videos.

