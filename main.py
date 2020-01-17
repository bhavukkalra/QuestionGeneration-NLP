import aqgFunction
import pandas as pd
def main():
        # Create AQG object
        aqg = aqgFunction.AutomaticQuestionGenerator()

        # Enter input Text File PATH
        # inputTextPath = "DB/db.txt"
        # readFile = open(inputTextPath, 'r+')
        # inputText = readFile.read()
        a = pd.read_csv('mydata.csv',names = ["titles","paragraphs"])
        column_length = len(a['paragraphs'])
        for i in range(14900,column_length):
            inputText = a["paragraphs"][i]
            questionList = aqg.aqgParse(inputText)
            aqg.display(questionList)
        

        # questionList = aqg.aqgParse(inputText)
        # aqg.display(questionList)

        return 0


    # Call Main Function
if __name__ == "__main__":

    main()


  # Main Function
    
