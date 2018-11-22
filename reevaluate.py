#!/usr/bin/env python

import os
from datetime import datetime
import shutil


def prnt(message):
    print datetime.utcnow().strftime('[ %Y-%m-%d %H:%M:%S.%f ] => ') + message


def main():
    prnt("re evaluating the web storm")
    prnt("finding files and folders")
    prnt("works on linux")
    this_is_the_folder, home_dir = files_and_folders()
    if this_is_the_folder is not "":
        make_changes(this_is_the_folder, home_dir)
    else:
        prnt("no folder found. exiting...")


def make_changes(f, home):
    prnt("deleting the evaluating files.")
    file_to_delete = os.listdir(home + "/" + f + "/config/eval/")
    for ff in file_to_delete:
        os.remove(home + "/" + f + "/config/eval/" + ff)
    prnt("deleting evaluation line from options.xml")
    opts = open(home + "/" + f + "/config/options/options.xml", "r+")
    lines = opts.readlines()
    opts.seek(0)
    for line in lines:
        if "name=\"evls" not in line:
            opts.write(line)
    opts.truncate()
    opts.close()
    prnt("removing the webstorm folder")
    shutil.rmtree(home + "/" + ".java/.userPrefs/jetbrains/webstorm")
    prnt("please restart your webstorm")


def files_and_folders():
    list_dir = os.listdir(os.path.expanduser("~"))  # cool
    webstorm_dir = ""
    for d in list_dir:
        if ".WebStorm" in d:
            webstorm_dir = d
            prnt("cool found the folder %s" % webstorm_dir)
            return webstorm_dir, os.path.expanduser("~")
    return ""


if __name__ == '__main__':
    main()
