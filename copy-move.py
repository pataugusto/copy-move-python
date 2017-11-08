# -*- coding: utf-8 -*-
# @Author: patrick hestad
# @Date:   2017-11-08 20:56:47
# @Last Modified by:   patri
# @Last Modified time: 2017-11-08 22:31:11

import os
import time
import shutil
import logging
from logging.handlers import RotatingFileHandler
from logging import handlers
import sys

log = logging.getLogger('')
log.setLevel(logging.DEBUG)
format = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]:  %(message)s")

ch = logging.StreamHandler(sys.stdout)
ch.setFormatter(format)
log.addHandler(ch)



def copy_files(file_list, dst, sleep=5):
	for src in file_list:
		shutil.copy2(src, dst) # target filename is /dst/dir/file.ext
		log.info(src + " copied.")
		log.info("Sleeping for %d seconds.", sleep)
		time.sleep(sleep)


def get_file_list(src):
	arr_txt = [src+i for i in os.listdir(src) if i.endswith(".txt")]
	return arr_txt


if __name__ == '__main__':
	start_time = time.time()

	src = "C:\\Users\\patri\\Desktop\\testfolder\\" 	# Source
	dst = "C:\\Users\\patri\\Desktop\\output\\"			# Destination
	
	file_list = get_file_list(src)		# Get all files in source folder

	for i in file_list:
		print(i)

	copy_files(file_list, dst)			# Copy all files to destination


	log.info("Script executed in %.4f seconds" % (time.time() - start_time))
