hello = input("Hello, What is your name? : \n")
print("Welcome", hello, "!")

print('This is a quiz that seeks to test your general knowledge. It includes fill-in questions, True or False '
      'statements and Multiple Choice Questions \n')

num_of_questions = int(input("How many questions do you want to answer?: \n"))

print("Okay then! Enjoy the quiz", hello, '\n')

import random


def get_tof_statements():
    statements = []
    statements.append(["Apple is the first trillion dollar company. True or False?:  ", "true"])
    statements.append(["Graham Potter has worked for Ghana before. True or False?:  ", "true"])
    statements.append(
        ["The depreciation of the cedi against the dollar is mainly due to The Russian-Ukraine war. True or False?:  ",
         "false"])
    statements.append(["In addition to Twitter, Elon Musk also owns Instagram. True or False?:  ", "false"])
    statements.append(["The largest living frog is the Goliath frog of West Africa. True or False?:  ", "true"])
    statements.append(["South Africa has one capital. True or False?:  ", "False"])
    statements.append(["Greenland is the largest island in the world. True or False?:  ", "true"])
    statements.append(["Humans lose an average of 75 strands in one day.True or False?:  ", "false"])
    statements.append(["Beauty and the Beast was Disney's first broadway musical. True or False?:  ", "true"])
    statements.append(["Cheesecakes comes from Italy.True or False?: ", "false"])

    return statements


def get_fill_in_questions():
    questions = []
    questions.append(["In what year did Ghana gain independence", "1957"])
    questions.append(["How old was Kwame Nkrumah when He died?", "62"])
    questions.append(["Who has the most goals in football history ", "cristiano ronaldo"])
    questions.append(["How many Balon Dors does Lionel Messi have", "7"])
    questions.append(["What country has the highest life expectancy", "hong kong"])
    questions.append(["What is the most common surname in the US", "smith"])
    questions.append(["What artiste has the most streams on Spotify", "drake"])
    questions.append(["How many elements are on the periodic table", "118"])
    questions.append(["What country has the most World Cups", "brazil"])
    questions.append(["Kratos is the main character of what video game series", "god of war"])

    return questions


def get_mcq_questions():
    mcqs = []
    mcqs.append(["Which of the following is not associated with the UNO\n a. ILO \n b. WHO\n c. ASEAN\n d. All of the "
                 "above", "asean", "c"])
    mcqs.append(
        ["Our country is a spiritual country. Theirs ....... religious\n a. is \n b. are\n c. also\n d. have", "is",
         "a"])
    mcqs.append(["Please, come ...... the bathroom\n a. out of \n b. over\n c. on\n d. in", "out of", "a"])
    mcqs.append(
        ["........ is the tulip capital of the world\n a. USA \n b. Greenland\n c. Netherlands\n d. Switzerland",
         "netherlands", "c"])
    mcqs.append(["Penalty cards(Yellow,Red) used in Football was introduced in the year : \n a. 1970 \n b. 1974\n c. "
                 "1996\n d. 1990", "1970", "a"])
    mcqs.append(["How many keys has a standard keyboard\n a. 2 \n b. 47\n c. 66\n d. 24", "2", "a"])
    mcqs.append(
        ["The largest desert in the world is\n a. Sahara \n b. Arctic\n c. Antarctica\n d. Atacama", "antarctica", "c"])
    mcqs.append(["Code name of the operation of killing Osama Bin laden was \n a. Rolling Thunder \n b. Thunderbolt\n "
                 "c. "
                 "Wrath of God\n d. Neptune Spear", "neptune spear", "d"])
    mcqs.append(["The part of the eye on which images are focused like film in a camera is \n a. Cornea \n b. lens\n "
                 "c. Pupil\n d. Retina", "retina", "d"])
    mcqs.append(
        ["The first convert to Islam was a ........\n a. Boy \n b. Companion\n c. Lady\n d. Slave", "lady", "a"])

    return mcqs


def play_tof_quiz():
    player_score = 0

    tof_statements = get_tof_statements() + get_mcq_questions() + get_fill_in_questions()

    random.shuffle(tof_statements)

    d = 1

    for x in range(num_of_questions):
        print(d, ".", tof_statements[x][0])
        guess = input()
        guess = guess.lower()
        d += 1
        if guess == tof_statements[x][1]:
            print("Correct!")
            player_score += 1
        else:
            print("Wrong!")

    print("Well done! You got", player_score, "out of", num_of_questions, "!")


play_tof_quiz()
