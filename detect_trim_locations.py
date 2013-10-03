def Trim_Locations(qualities, threshold):
    '''Takes as input the list of average quality scores within each window
    that was produced by the function av_window_quality
    Then finds the index of the first item in the list above the threshold
    and the index of the last item in the list above the threshold.
    Output: two numbers to be used as the trim positions.'''
    
