STEP 1: Install pyautogui and pillow:
 go to cmd and type-> pip3 install pyautogui
                   -> pip3 install pillow



CODE EXPLANATION:
creating rectangles:
take a screenshot and follow steps below (for 1920 X 820 screen)
Draw the rectangle for cactus
         for i in range(530, 610):
             for j in range(130, 160):
                  data[i, j] = 0
        
     Draw the rectangle for birds
         for i in range(530, 560):
             for j in range(100, 125):
                 data[i, j] = 171

         image.show()
         break


