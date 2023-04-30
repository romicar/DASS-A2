# import numpy as np
# tree = "🌳"
# from colorama import Back, Fore,Style
# # print(len(tree))
# a = np.full((3,4),"🌲")
# a[2,3] = Back.CYAN + "+" + Back.RESET

# arr = [[" " for i in range(4)] for j in range(3)]
# arr[2][0] = Back.CYAN + "+" + Back.RESET
# # print(arr[2][0])
# # print(arr)
# # print(a.size)
# # print(a)
# # for i in range(3):
# #     for j in range(4):
# #         print(arr[i][j],end="")
# #     print("")

# # arr[0][0] = 9
    
# # print(arr)


# a = []
# a = [[' ','/','\\',' '],['/','_','_','\\'],['|',' ',' ','|'],['|','_','_','|']]
# for i in range(4):
#     for j in range(4):
#         print(a[i][j],end="")
#     print("")




# # from pynput import keyboard

# # def on_press(key):
# #     try:
# #         print('Alphanumeric key pressed: {0} '.format(
# #             key.char))
# #     except AttributeError:
# #         print('special key pressed: {0}'.format(
# #             key))

# # def on_release(key):
# #     print('Key released: {0}'.format(
# #         key))
# #     if key == keyboard.Key.esc:
# #         # Stop listener
# #         return False

# # # Collect events until released
# # with keyboard.Listener(
# #         on_press=on_press,
# #         on_release=on_release) as listener:
# #     listener.join()











#         #   /\
#         #  /__\
#         #  |  |
#     #  +   #  |__|
#     #  o  
#     # (|)
#     # / \
    
    
    
A = {"walls":[(1,2),(3,4)],"buildings" : [(4,5),(2,3)]}

print(A["walls"][0])


def text():
    for i in range(5):
        if i == 8:
            return i
        
print(text())