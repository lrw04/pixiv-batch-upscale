# pixiv-batch-upscale

This utility takes listed illustrations from a larger collection as created by [Nandaka/PixivUtil2](https://github.com/Nandaka/PixivUtil2) and upscales each of them using [nihui/waifu2x-ncnn-vulkan](https://github.com/nihui/waifu2x-ncnn-vulkan) until it is of at least a specified size.

## Usage

First specify the path to the upscaler binary in `config.py`.

Write a list of desired illustrations. The list should contain lines in the following format:

```
pid,index
```

Alternatively, if you have a folder of images with filenames in the same format as the downloader  uses, you can run `python readlist.py <dir>`. The list will be put into stdout.

To start upscaling, run `python batchupscale.py <imagesdir> <listfile> <outdir> <size>` to retrieve images from `<imagedir>`, leaving only those listed in `<listfile>`, putting them in `<outdir>`, and upscale them until they are each at least of size `<size>` (in MiB) or when the program has already tried 5 times.

The program is tested only under Windows 10.