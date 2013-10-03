def Trim_Locations(qualities, threshold):
    '''Takes as input the list of average quality scores within each window
    that was produced by the function av_window_quality
    
    Then finds the index of the first item in the list above the threshold
    and the index of the last item in the list above the threshold.
    
    Output: two numbers to be used as the first and second trim positions respectively.
    
    Trim_Locations([Int] Int) -> [Int]
    '''
    assert isinstance(qualities, list) == True
    assert isinstance (threshold, int) == True
    
    for i in range(qualities.len):
        if qualities[i] >= threshold:
            return i
    
    first_trim_location = i
    
    for j in range(qualities.len):
        if qualities.reverse[j] >= threshold:
            return j
    
    second_trim_location = qualities.len-j
    
    assert Trim_Locations([20, 30, 31, 30, 29], 30) == [1,4]
    
    return [first_trim_location, second_trim_location]
    

def Output_FastQ(input_read, trim_locations):
    '''Makes a new object of class 'fastq_read' using the original object
    and trimming the sequence and the quality strings according to trim_locations.
    
    Also appends the string '_trimmed' to the name.
    Output_FastQ(fastq_read, [Int]) -> fastq_read
    '''
    assert isinstance(input_read, fastq_read)
    assert isinstance (trim_locations, list)
    
    output_read = fastq_read
    
    output_read.name = input_read.name + '_trimmed'
    output_read.nucleotides = input_read.nucleotides[trim_locations[0]:trim_locations[1]]
    output_read.qualities = input_read.qualities[trim_locations[0]:trim_locations[1]]
    
    return output_read
