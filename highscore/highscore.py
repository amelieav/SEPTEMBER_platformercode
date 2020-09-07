import random
final_score = random.randint(1, 200)

with open("scores.txt", "r") as f:
    file_length = len(f.readlines())
    file_length = str(file_length+1)
    new_player_number = ("player" + file_length)

print(new_player_number)

dict = {new_player_number:final_score}
print(dict)
with open("scores.txt", "a") as f:
    f.write(str(dict))
    if int(file_length) >= 1:
        f.write('\n')

def scorestodict():
    # with closes the file when the block of code ends
    with open("scores.txt", "r") as f:
        mydict = {}  # create a dictionary called mydict
        for line in f:
            key, val = line.strip("\"\n{}").split(":")
            mydict[key.strip("'")] = val.strip()
    print(mydict)  # test
    print("Player 1 score is: " + mydict["player1"])
    return mydict
def highestscore(mydict):
    ordered_scores = sorted(mydict.items(), key=lambda x:x[1], reverse=True)
    print(ordered_scores)
    top_score = list(ordered_scores)[0]
    player_id = top_score[0]
    score_id = top_score[1]
    print("Second score is: ", score_id, "    Attained by: ", player_id )


scorestodict()
highestscore(mydict=scorestodict())