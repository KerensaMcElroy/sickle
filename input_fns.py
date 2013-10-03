

def prompt_inp(prompt_str):
    in_str = raw_input(prompt_str)
    return in_str

def get_window_lth(read_lth):
    '''Function takes read length as input and prompts user for window length.
    If window length not valid, default value of 0.1 * read length is returned'''
    prompt_str = "Enter a window length (default is read_length/10): "
    lth = int(raw_input(prompt_str))
    if not (lth > 0 and lth <= read_lth):
        lth = read_lth/10
    return lth

def ask_qual_thresh():
    prompt_str = "Enter a quality threshold (1-40): "
    thresh = 0
    while not (thresh >=1 and thresh <=40):
        thresh = float(raw_input(prompt_str))
    return thresh

out_var = get_window_lth(120)
print "You entered: ", out_var

out_var = ask_qual_thresh()
print "You entered: ", out_var
