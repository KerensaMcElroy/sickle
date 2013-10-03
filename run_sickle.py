from better_sickle_kerensa import *
from detect_trim_locations import *
from input_fns import *
from av_window_quality import *
from Team1_sickle.py import *

#get input file
input_file = prompt_inp()

#convert first four reads into a fastq_read object
input_fastq_objs = parse_file(input_file)

# get quality threshold
thresh = ask_qual_thresh()

# get window length

window_length = get_window_length(100)

for fastq_obj in input_fastq_objs:

# decode quality string

    decoded = decode_quality(fastq_obj.qual_seq, 33)

# calculate average quality across windows
    average_qualities = Av_Window_Quality(decoded, window_length)

# identify trim locations by comparison to threshold value
    trim_locations = Trim_Locations(average_qualities,thresh)

# make output object
#output = Output_FastQ(input_fastq, trim_locations)

#print output
