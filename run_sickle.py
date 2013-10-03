from better_sickle_kerensa import *
from detect_trim_locations import *
from input_fns import *
from av_window_quality import *
from Team1_sickle.py import *

#get input file
input_file = prompt_inp()

#convert first four reads into a fastq_read object
input_fastq = get1block(input_file)

# get window length
# user input
window_length = get_window_length(,len(input_fastq.nucleotide))

# get quality threshold
thresh = ask_qual_thresh()

# decode quality string
# 
decoded = decode_quality(quality_string, offset)

# calculate average quality across windows
average_qualities = Av_Window_Quality(decoded, lth)

# identify trim locations by comparison to threshold value
trim_locations = Trim_Locations(average_qualities,thresh)

# make output object
output = Output_FastQ(input_fastq, trim_locations)

print output
