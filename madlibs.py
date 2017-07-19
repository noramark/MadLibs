def story_answers():

  answers = []

  answers.append(raw_input("place: "))
  answers.append(raw_input("relative: "))
  answers.append(raw_input("name: "))
  answers.append(raw_input("adjective: "))
  answers.append(raw_input("adjective: "))
  answers.append(raw_input("adjective: "))
  answers.append(raw_input("place: "))
  answers.append(raw_input("number: "))
  answers.append(raw_input("plural noun: "))
  answers.append(raw_input("verb: "))
  answers.append(raw_input("person: "))
  answers.append(raw_input("feeling: "))
  answers.append(raw_input("person: "))
  answers.append(raw_input("place: "))
  answers.append(raw_input("verb: "))

  return answers


def main(story):

    print "Let's play Madlibs!!1! \n \n"
    answers = story_answers()
    print story.format(*answers)

    return

story = '''
Today I went to {} with my {} {}.
The weather was {}, {}, and {}.
We hit the  together and won {} {}
We decided that she was not {} with the {}.
I hope she is {} with that {}.
As the night came we decided to go to a {} where people like to {}.

'''
main(story)
