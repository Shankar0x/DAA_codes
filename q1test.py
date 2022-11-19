from graph_class import worder

def q1(wordObj):
    wordObj.gridfinder()

def q2(wordObj):
    wordObj.wordfinder('a')
    wordObj.wordfinder('s')

def main():
    dict1 =  ['an', 'and', 'bad', 'badge','ban', 'band', 'bane', 'bang',
    'bangs', 'bans', 'be', 'bean', 'beans', 'bear', 'beard', 'beards',
    'bee', 'been', 'beep', 'beeps', 'bees', 'dab', 'dabs', 'dane',
    'danes', 'darn', 'drab', 'ear', 'earn', 'earns', 'end', 'ends',
    'grad', 'grads', 'he', 'pen', 'pend', 'pens', 'ran', 'rang', 'range', 'see', 'seen', 'seep', 'she' ]
    word_grid=[
      ['e','f','r','a'],
      ['h','g','d','r'],
      ['p','s','n','a'],
      ['e','e','b','e']
    ]

    wordObj=worder(word_grid,dict1)
    q1(wordObj)
    q2(wordObj)
        
    
if __name__ == '__main__':
    main()

