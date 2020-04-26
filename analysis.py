from textblob import TextBlob

_polarity_low=-0.5
_polarity_high=0.5

_subjectivity_low=0.25
#vague data
_subjectivity_high=0.75
#very descriptive data

def analysisInfo(line):
    tb=TextBlob(line)
    polarity=tb.sentiment.polarity
    subjectivity=tb.sentiment.subjectivity
    
    print('polarity =', polarity, end='\t')
    if polarity<=_polarity_low:
        print('Negative view') 
    elif polarity<_polarity_high:
        print('Neutral view')
    else:
        print('Positive view')


    print('subj =',subjectivity, end='\t')    
    if subjectivity<=_subjectivity_low:
        print('vague data') 
    elif subjectivity<_subjectivity_high:
        print('normal description')
    else:
        print('descriptive data')
    



def main():
    file=open('news.txt', 'r')
    line=file.read()
    print(line)
    tb=TextBlob(line)
    #print(tb.sentiment)

    print('polarity =',tb.sentiment.polarity)
    print('subj =',tb.sentiment.subjectivity)

if __name__=='__main__':
    main()

