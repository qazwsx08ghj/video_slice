import argparse


def return_argument():

    parser = argparse.ArgumentParser(
        description="Slice video"
    )



    parser.add_argument(
        "-v", "--video",
        metavar="",
        help="The video path that you want to slice",
    )

    parser.add_argument(
        "-f", "--fps",
        metavar="", type=int,
        help="Insert an integer. How many picture you want in a second, default:1.", default=1
    )

    # path for slice picture
    parser.add_argument(
        "-p", "--path",
        metavar="",
        help="The path you want to save sliced picture."
    )

    # choose train_test usage, may add vaild
    parser.add_argument(
        "-u", "--usage",
        metavar=" ", choices=["train", "test", 'train_test'], default="train", type=str,
        help="How to save picture, default= train."
    )

    # customise train test split
    parser.add_argument(
        "-r", "--ratio",
        metavar="", default=(0.75, 0.25), type=tuple,
        help="Tuple type to save float, like (0.75, 0.25). Any %% you want to split image to train test."
    )

    # handling train test path
    parser.add_argument(
        "-Tp", "--train_dir_path",
        metavar="", type=str, default="train/",
        help="Where your train image you want to save."
    )

    parser.add_argument(
        "-tp", "--test_dir_path",
        metavar="", default="test/", type=str,
        help="Where your test image you want to save."
    )

    return parser.parse_args()
