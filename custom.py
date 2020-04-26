class Custom:
    def __init__(self):
        self.autoPlay=-1
        self.immidiateAnalysis=False
        self.detailed=True
        self.endOfNewsDelmiter='--'+':'*10 + '--'
        self.startOfLine='\t'

    def verboseCustomize(self):
        self.autoPlay=4
        self.immidiateAnalysis=True
        self.detailed=True
        return 1

        if (input('Do you want Autoplay (Y/N) [default: N]: ').upper() or 'N') == 'Y':
            self.autoPlay=int(input('Mention Autoplay time in seconds: '))
        if (input('Perform Analysis and Display sentiment as you go through news(Y/N) [default: N]: ').upper() or 'N') == 'Y':
            self.immidiateAnalysis=True
        if input('Show detailed News: ').upper() == 'Y':
            self.detailed=True
        self.startOfLine=input('Specify start of line string [default]: ') or self.startOfLine
        self.endOfNewsDelmiter=input('Specify end of news delimiter [default]: ') or self.endOfNewsDelmiter
