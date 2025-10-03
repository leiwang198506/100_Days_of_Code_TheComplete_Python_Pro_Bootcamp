print(r'''




                        /\
                        ||
                        ||
                        ||
                        ||                                               ~-----~
                        ||                                            /===--  ---~~~
                        ||                   ;'                 /==~- --   -    ---~~~
                        ||                (/ ('              /=----         ~~_  --(  '
                        ||             ' / ;'             /=----               \__~
     '                ~==_=~          '('             ~-~~      ~~~~        ~~~--\~'
     \\                (c_\_        .i.             /~--    ~~~--   -~     (     '
      `\               (}| /       / : \           / ~~------~     ~~\   (
      \ '               ||/ \      |===|          /~/             ~~~ \ \(
      ``~\              ~~\  )~.~_ >._.< _~-~     |`_          ~~-~     )\
       '-~                 {  /  ) \___/ (   \   |` ` _       ~~         '
       \ -~\                -<__/  -   -  L~ -;   \\    \ _ _/
       `` ~~=\                  {    :    }\ ,\    ||   _ :(
        \  ~~=\__                \ _/ \_ /  )  } _//   ( `|'
        ``    , ~\--~=\           \     /  / _/ / '    (   '
         \`    } ~ ~~ -~=\   _~_  / \ / \ )^ ( // :_  / '
         |    ,          _~-'   '~~__-_  / - |/     \ (
          \  ,_--_     _/              \_'---', -~ .   \
           )/      /\ / /\   ,~,         \__ _}     \_  "~_
           ,      { ( _ )'} ~ - \_    ~\  (-:-)       "\   ~ 
                  /'' ''  )~ \~_ ~\   )->  \ :|    _,       " 
                 (\  _/)''} | \~_ ~  /~(   | :)   /          }
                <``  >;,,/  )= \~__ {{{ '  \ =(  ,   ,       ;
               {o_o }_/     |v  '~__  _    )-v|  "  :       ,"
               {/"\_)       {_/'  \~__ ~\_ \\_} '  {        /~\
               ,/!          '_/    '~__ _-~ \_' :  '      ,"  ~ 
              (''`                  /,'~___~    | /     ,"  \ ~' 
             '/, )                 (-)  '~____~";     ,"     , }
           /,')                    / \         /  ,~-"       '~'
       (  ''/                     / ( '       /  /          '~'
    ~ ~  ,, /) ,                 (/( \)      ( -)          /~'
  (  ~~ )`  ~}                   '  \)'     _/ /           ~'
 { |) /`,--.(  }'                    '     (  /          /~'
(` ~ ( c|~~| `}   )                        '/:\         ,'
 ~ )/``) )) '|),                          (/ | \)                 -sjm
  (` (-~(( `~`'  )                        ' (/ '
   `~'    )'`')                              '
     ` ``

''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction=input('You\'re at a cross road. '
                'Where do you want to go? Type "left" or "right"\n').lower() #lowe()make answers lowercase.
if direction == "left":
    lake_answer=input('You\'ve come to a lake. '
                      'There is an island in the middle of the lake. '
                      'Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if lake_answer == "wait":
        door_answer=input("You arrive at the island unharmed. "
                          "There is a house with 3 doors."
                          "One red, one yellow and one blue. "
                          "Which colour do you choose?\n").lower()
        if door_answer == "red":
            print("It's a room full of fire. Game Over.")
        elif door_answer == "blue":
            print("You enter a room of beasts. Game Over.")
        elif door_answer =="yellow":
            print("you found the treasure! You Win!")
        else:
            print("Your input is not valid. Game Over.")
    elif lake_answer == "swim":
        print("You get attacked by an angry trout. Game Over.")
    else:
        print("Your input is not valid. Game Over.")
elif direction=="right":
    print ("You fall into a hole. Game Over. ")
else:
    print("Your input is not valid. Game Over.")


