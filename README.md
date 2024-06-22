# Smart glove for speech impaired individuals

## Features
1. Flex sensor based detection of signs and custom android app for text and audio output (using MIT app inventor)
2. Employs fingerspelling, a new mode of communication employing 3 modes and entire device is operated with signs, including START and STOP
   a. 3 Modes each having 32 options to select
   b. Mode 1 - common phrases
   c. Mode 2 - alphabets
   d. Mode 3 - Numbers and special characters
   e. Start and Stop
3. Custom created dataset of ADC values from 100 individuals -  total 32000 set of values, each class 1000 values
4. ML algorithms embedded to increase the accuracy from 79% to 91%

## References 
1. [Report submitted for Final year project - ](https://github.com/Dharun235/Smart-glove-for-speech-impaired/blob/main/Final%20Report.pdf)
2. [Dataset - ](https://github.com/Dharun235/Smart-glove-for-speech-impaired/blob/main/final_dataset_file.xlsx)
3. [Image of signs - ](https://github.com/Dharun235/Smart-glove-for-speech-impaired/tree/main/Image%20of%20signs)
4. [Dataset analysis and ML application on the dataset - ](https://github.com/Dharun235/Smart-glove-for-speech-impaired/blob/main/ml_analysis_on_dataset.ipynb)
5. [Code for quickly finding which ML models to use among many of the ML models using LAZY PREDICT library](https://github.com/Dharun235/Smart-glove-for-speech-impaired/blob/main/lazy-predict.py)

## Codes
1. [Data collection from arduino (ADC values)](https://github.com/Dharun235/Smart-glove-for-speech-impaired/blob/main/arduino_logger.ino)
2. [Sending the output to app](https://github.com/Dharun235/Smart-glove-for-speech-impaired/blob/main/arduino_sender.ino)
3. [Read data from arduino](https://github.com/Dharun235/Smart-glove-for-speech-impaired/blob/main/read_from_arduino.py)
4. [Flex sensor ADC value to decimal number convertor](https://github.com/Dharun235/Smart-glove-for-speech-impaired/blob/main/flex_to_num.py)
5. [Main loop](https://github.com/Dharun235/Smart-glove-for-speech-impaired/blob/main/Main%20loop.py)
