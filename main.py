import pygame
import sys
import os
import csv
import datetime

def main():
    pygame.init()
    clock = pygame.time.Clock()
    fps = 60
    size = [320, 400]
    bg = [68,217,230]
    color = [255,255,255]
    color2 = [0,0,0]
    text=""
    font = pygame.font.Font(None, 32)

    screen = pygame.display.set_mode(size)
    myimage = pygame.image.load('blood_G.jpg')
    myimage1 = pygame.image.load('blood_P.jpg')
    myimage2= pygame.image.load('excercise.jpg')
    myimage3 = pygame.image.load('diet.jpg')
    imagerect=myimage.get_rect()
    imagerect1=myimage1.get_rect()
    place1=pygame.Rect(imagerect.left+10,imagerect.top+60,imagerect.right,imagerect.bottom)
    imagerect2=myimage2.get_rect()
    place2=pygame.Rect(imagerect1.left+160,imagerect1.top+60,imagerect1.right,imagerect1.bottom)
    imagerect3=myimage3.get_rect()
    place3=pygame.Rect(imagerect2.left+10,imagerect2.top+210,imagerect2.right,imagerect2.bottom)
    place4=pygame.Rect(imagerect3.left+160,imagerect3.top+210,imagerect3.right,imagerect3.bottom)
    option=0
    input_box = pygame.Rect(100, 100, 140, 32)
    button_submit = pygame.Rect(200,150,100,50)
    input_active=False
    filename='data.csv'
	
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position

                # checks if mouse position is over the button
                if option==0:
                    if place1.collidepoint(mouse_pos):
                        # prints current location of mouse
                        option=1
                        print('button 1 was pressed at {0}'.format(mouse_pos))
					
                    elif place2.collidepoint(mouse_pos):
                        print('button 2 was pressed at {0}'.format(mouse_pos))
					
                    elif place3.collidepoint(mouse_pos):
                        print('button 3 was pressed at {0}'.format(mouse_pos))
					
                    elif place4.collidepoint(mouse_pos):
                        print('button 4 was pressed at {0}'.format(mouse_pos))
				
                elif option==1:
                    if input_box.collidepoint(mouse_pos):
                        input_active=not input_active
                        print('collide')
                    else:
                        input_active=not input_active
						
                    if button_submit.collidepoint(mouse_pos):
                        print('')
                        file_exists = os.path.isfile(filename)
		
                        with open (filename,'a') as csvfile:
                            fieldnames = ['Time', 'Glucose']
                            writer = csv.DictWriter(csvfile,delimiter=',',lineterminator='\n' ,fieldnames=fieldnames)
                            if not file_exists:
                                writer.writeheader()
                            writer.writerow({'Time': datetime.datetime.now(), 'Glucose': text})
						
            if event.type == pygame.KEYDOWN:
                if input_active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]	
                    else:
                        text += event.unicode

        screen.fill(bg)
        if (option==0):
            screen.blit(myimage,place1 )
            screen.blit(myimage1,place2)
            screen.blit(myimage2,place3 )
            screen.blit(myimage3, place4)
            
        elif (option==1):
            pygame.draw.rect(screen, color, input_box, 2)
            txt_surface = font.render(text, True, color)
            txt_surface2 = font.render("Glucose:", True, color)
            width = max(200, txt_surface.get_width())
            input_box.w = width
            # Blit the text
            screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
            screen.blit(txt_surface2, (0,input_box.y))
            pygame.draw.rect(screen,color,(200,150,100,50))
            txt_surface3 = font.render("SUBMIT", True, color2)
            screen.blit(txt_surface3, (210,150))
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    sys.exit


if __name__ == '__main__':
    main()