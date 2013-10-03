def Av_Window_Quality(quality_decoded, window_len):
    '''This is a function to determine the average base quality
    within each window of length 'window_len', which was input by the user.
    It takes an input list of quality scores in integer form
    called 'quality_decoded', inherited from function XXXX.
    
    Av_Window_Quality moves along the quality score list one element at a time.
    
    Output is a list of average quality scores with indices
    corresponding to the window start position. '''
    
    assert isinstance(quality_encoded, lst) == True
    assert isinstance(window_len, int) == True
    
#    window_start = []
#    window_end = []
    average_quality = []

    for i in range(quality_decoded.len):
        # Keeping this code in case we want to track the window start and end later...
        # window_start.append(i)
        # temp_window_end = i + window_len - 1
        # window_end.append(temp_window_end)
        
        # Cut the list of quality scores to the current window
        quality_window = quality_decoded[i:i+window_len]
        average_quality.append(sum(quality_window)/float(window_len))
    return average_quality
assert Av_Window_Quality([10,20,30,40],3) == [20,30]


# qualities=Av_Window_Quality(my_q_d, my_w_l)
