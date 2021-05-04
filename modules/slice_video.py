import cv2
import splitfolders
import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


def save_img(**kwargs):
    try:
        if not os.path.exists(os.path.join(BASE_DIR, kwargs["path"])) or os.path.exists(kwargs["path"]):
            os.makedirs(kwargs["path"])
    except FileExistsError:
        pass
    p = str(kwargs["id"]) + ".jpg"
    cv2.imwrite(os.path.join(BASE_DIR, kwargs["path"]) + p, kwargs["image"])
    print("success to save image {} to {}".format(p, os.path.join(BASE_DIR, kwargs["path"])))


def slice_vid(**kwargs):
    video = cv2.VideoCapture(kwargs["video"])
    vLeng = video.get(7)
    # vFps = video.get(int(cv2.CAP_PROP_FPS))
    
    frame_counter = 1
    video.set(1, vLeng)
    watch, vFrame = video.read()
    frame = kwargs["fps"]

    id = int()

    if type(kwargs["path"]) == list:
        while watch:
            if frame_counter % frame == 0:
                id += 1
                save_img(image=vFrame, id=id, path=kwargs["path"][0])
            watch, vFrame = video.read()
            frame_counter = frame_counter + 1
        splitfolders.ratio(kwargs["path"][0], output=kwargs["path"][1], ratio=kwargs["ratio"])

    else:
        while watch:
            watch, vFrame = video.read()

            if frame_counter % frame == 0:
                id += 1
                save_img(image=vFrame, id=id, path=kwargs["path"])
            frame_counter = frame_counter + 1

        # release video for the last of picture, because that weak cpu

def option(args):
    if args.path is None and args.usage is None:
        slice_vid(video=args.video, fps=args.fps, path=r"train\"")

    elif args.path is not None:
        try:
            if args.path is not None:
                if args.path[-1] is not "/":
                    args.path = args.path + "/"
                    slice_vid(
                        video=args.video, fps=args.fps, path=args.path
                    )
                else:
                    slice_vid(
                        video=args.video, fps=args.fps, path=args.path
                    )
        except TypeError:
            print(args.path)
    elif args.usage is "train":
        if args.train_dir_path is not None:
            if args.train_dir_path[-1] is not "/":
                args.train_dir_path = args.train_dir_path + "/"
                slice_vid(
                    video=args.video, fps=args.fps, path=args.train_dir_path
                )
            else:
                slice_vid(
                    video=args.video, fps=args.fps, path=args.train_dir_path
                )

    elif args.usage is "test":
        if args.test_dir_path is not None:
            if args.test_dir_path[-1] is not "/":
                args.test_dir_path = args.test_dir_path + "/"
                slice_vid(
                    video=args.video, fps=args.fps, path=args.test_dir_path
                )
            else:
                slice_vid(
                    video=args.video, fps=args.fps, path=args.test_dir_path
                )

    elif args.usage is "train_test":
        if args.train_dir_path is None:
            slice_vid(
                video=args.video, fps=args.fps, path=["train/", "test/"], ratio=args.ratio
            )

        elif args.train_dir_path is not None:
            slice_vid(
                video=args.video, fps=args.fps, path=[args.train_dir_path, args.test_dir_path], ratio=args.ratio
            )

    elif args.usage is None:
        slice_vid(
            video=args.video, fps=args.fps, path="train/"
        )


if __name__ == "__main__":
    pass
