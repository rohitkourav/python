def game():
    return 446

score = game()
with open("hiscore.txt") as f:
    hiScoreStr = f.read()
if hiScoreStr=='':
    with open("hiscore.txt",  "w") as f:
        f.write(str(score))

if int(hiScoreStr)<score or hiScoreStr=='':
    with
     open("hiscore.txt", "w") as f:
        f.write(str(score))