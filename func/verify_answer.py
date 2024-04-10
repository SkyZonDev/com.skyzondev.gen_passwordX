def verify_answer(answer, index, excluding_char):
    answerPos = ["yes", "y", "oui", "o", "1"]
    answerNeg = ["no", "n", "non", "n", "0"] # I add 2 "n" for avoid the out of range error
    for i in range(len(answerPos)):
        if answerPos[i] == answer: return True
        elif answerNeg[i] == answer: 
            excluding_char.append(index)
            return False
    return False
