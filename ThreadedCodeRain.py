import os, time, random, threading

x = ['0', '1', '2', '3' ,'4', '5', '6', '7']
y = ['8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

names = ['Allah', 'Uzumaki Naruto', 'WarKingMak', 'Neo', 'Minato', 'Jiraiya',
          'Kakashi', 'Python', '1337', 'Hacker', 'War', 'Peace', 'Samurai',
          'Luffy', 'Light', 'Rasen Shuriken', 'Bijuu Dama', 'Frog Kumite',
          'Kunai', 'Sage Mode', 'Rasengan', 'Dench']

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
          '!', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '}', '[', ']', '~', '`', '|', "/", ':', ';', '"', '<', '>', '?',
          '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def ColorChange():
    while True:
        for _ in x:
            for __ in y:
                os.system('color ' + _ + __)
                time.sleep(0.5)    
    
def ChangeTitle():
    while True:
        name = str(random.choice(names))
        os.system('title ' + name)
        time.sleep(1)

def CodeMatrix():
    while True:
        RandomCharList = random.sample(chars, 40)
        print ' '.join(RandomCharList)    

TitleThread = threading.Thread(target = ChangeTitle)
MatrixThread = threading.Thread(target = CodeMatrix)
ColorThread = threading.Thread(target = ColorChange)

TitleThread.start()
MatrixThread.start()
ColorThread.start()
